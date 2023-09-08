import os
import moviepy.editor as mp
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont

# Set the path to the ImageMagick binary
image_magick_binary = "C:\\Program Files\\ImageMagick-7.1.1-Q16\\convert"  # Replace with the actual path
os.environ["IMAGEMAGICK_BINARY"] = image_magick_binary

# Function to generate an image with text and save it
def generate_image_with_text(text, output_path):
    # Create a blank image with a white background
    width, height = 2000, 4000
    background_color = (255, 255, 255)
    image = Image.new("RGB", (width, height), background_color)

    # Initialize the drawing context
    draw = ImageDraw.Draw(image)

    # Define a font and size
    font = ImageFont.truetype("arial.ttf", 50)

    # Define text color and position
    text_color = (0, 0, 0)  # Black
    text_position = (width // 50, height // 59)

    # Draw text on the image
    draw.text(text_position, text, fill=text_color, font=font)

    # Save the generated image
    image.save(output_path)

# Define the story with text and timing
story = [
    {
        "text": "Conclusion\n\nPakistan is a nation of contrasts, where rich history meets contemporary challenges, and natural beauty coexists with complex socio-political dynamics. While it grapples with various issues, Pakistan also offers a world of opportunities. As the country continues its journey, it remains a land of promise, poised to make its mark on the global stage. With careful planning, investment, and inclusive policies, Pakistan has the potential to fulfill its promise and rise as a beacon of progress in South Asia.",
        "duration": 15
    }
]

# ... Rest of the script remains the same

# Directory to save the generated images
image_dir = "generated_images"
os.makedirs(image_dir, exist_ok=True)

# Directory to save the audio files
audio_dir = "audio_files"
os.makedirs(audio_dir, exist_ok=True)

# Create video clips for each part of the story
clips = []
audio_clips = []

for index, part in enumerate(story):
    text = part["text"]
    duration = part["duration"]

    # Generate audio from text using gTTS
    audio_text = gTTS(text, lang='en')
    audio_path = os.path.join(audio_dir, f"audio_{index}.mp3")
    audio_text.save(audio_path)
    audio_clip = mp.AudioFileClip(audio_path)
    audio_clips.append(audio_clip)

    # Generate an image with text
    image_path = os.path.join(image_dir, f"image_{index}.png")
    generate_image_with_text(text, image_path)

    # Create an image clip and set its duration
    image_clip = mp.ImageClip(image_path)
    image_clip = image_clip.set_duration(duration)

    # Center align text and image on the screen
    text_clip = mp.TextClip(text, fontsize=50, color="white")
    text_clip = text_clip.set_duration(duration)
    video_clip = mp.CompositeVideoClip([text_clip, image_clip])

    clips.append(video_clip)

# Concatenate video clips to create the final video
final_clip = mp.concatenate_videoclips(clips, method="compose")

# Concatenate audio clips to create the final audio
final_audio = mp.concatenate_audioclips(audio_clips)

# Set the audio of the final video
final_clip = final_clip.set_audio(final_audio)

# Set the output video file name
output_video_file = "story_video.mp4"

# Write the final video to a file with fullscreen resolution
final_clip.write_videofile(
    output_video_file,
    fps=1500,
    codec='libx264',
    preset='ultrafast',
    threads=4,
    audio_codec='aac',
    audio_fps=44100,
    audio_nbytes=4,
    audio_bufsize=2000,
)

# Clean up temporary files
for index in range(len(story)):
    os.remove(os.path.join(image_dir, f"image_{index}.png"))
    os.remove(os.path.join(audio_dir, f"audio_{index}.mp3"))

print("Video generation complete. Check", output_video_file)
