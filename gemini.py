import google.generativeai as genai
import json

# get your API key from key.json = { "key": "api_key" }
with open("key.json") as f:
    api_key = json.load(f)["key"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")  # Você pode trocar pelo modelo desejado
response = model.generate_content("How are you?")

print(response.text.strip())