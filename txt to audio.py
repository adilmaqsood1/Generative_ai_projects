from gtts import gTTS
import os

# Define the story with text
story = [
   "Pakistan is a nation of contrasts, where rich history meets contemporary challenges, and natural beauty coexists with complex socio-political dynamics. While it grapples with various issues, Pakistan also offers a world of opportunities. As the country continues its journey, it remains a land of promise, poised to make its mark on the global stage. With careful planning, investment, and inclusive policies, Pakistan has the potential to fulfill its promise and rise as a beacon of progress in South Asia."
]

# Directory to save the audio files
audio_dir = "audio_files"
os.makedirs(audio_dir, exist_ok=True)

# Generate audio clips for each part of the story
audio_clips = []

for index, text in enumerate(story):
    audio_text = gTTS(text, lang='en')
    audio_path = os.path.join(audio_dir, f"audio_{index}.mp3")
    audio_text.save(audio_path)
    audio_clips.append(audio_path)

# Print the paths to the generated audio files
for index, audio_path in enumerate(audio_clips):
    print(f"Generated audio for part {index}: {audio_path}")
