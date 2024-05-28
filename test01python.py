from realtime_tts import RealtimeTTS
import speech_recognition as sr
from openai import OpenAI

tts = RealtimeTTS()
r = sr.Recognizer()
client = OpenAI(base_url="http://192.168.1.121:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
  model="TheBloke/Mistral-7B-Instruct-v0.2-GGUF",
  messages=[
    {"role": "user", "content": prompt+"Réponse en Français souhaitée."}
  ],
  temperature=0.7,
)

#print(completion.choices[0].message.content)
