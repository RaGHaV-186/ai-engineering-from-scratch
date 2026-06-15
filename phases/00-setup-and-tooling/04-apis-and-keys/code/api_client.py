import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_key(name):
    value = os.getenv(name)
    if not value:
        print(f"[warn] {name} not set")
    return value


def call_gemini(prompt):
    key = get_key("GEMINI_API_KEY")
    if not key:
        return None

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={key}"

    try:
        response = requests.post(
            url,
            json={"contents": [{"parts": [{"text": prompt}]}]},
        )
        data = response.json()

        if "error" in data:
            return f"[error] {data['error']['message'][:80]}"

        return data["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        return f"[exception] {e}"


if __name__ == "__main__":
    prompt = "What is a neural network in one sentence?"
    print(f"Prompt: {prompt}\n")
    result = call_gemini(prompt)
    print(f"Response: {result}")