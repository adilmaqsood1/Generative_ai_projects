from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os

_ : bool = load_dotenv(find_dotenv()) # read local .env file

client : OpenAI = OpenAI()

from openai.types.chat.chat_completion import ChatCompletion

def chat_completion(prompt : str )-> str:
 response : ChatCompletion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo-1106",
    )
# print(response)
#  print(response.choices[0].message.content)
 return response.choices[0].message.content
