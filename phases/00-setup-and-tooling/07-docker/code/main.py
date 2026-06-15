import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment")

client = genai.Client(api_key=api_key)

prompt = "Say hello in 3 different languages. Be brief."
print(f"Prompt: {prompt}\n")

response = client.models.generate_content(
    model="gemini-2.0-flash-lite",
    contents=prompt
)
print(f"Response:\n{response.text}")
