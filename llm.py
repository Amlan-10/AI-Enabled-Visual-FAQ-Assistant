
import requests

NVIDIA_API_KEY = "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"  # rotate your key; do not hardcode in source

BASE_URL = "https://integrate.api.nvidia.com/v1"
MODEL = "meta/llama-4-maverick-17b-128e-instruct"

def generate_explanation(extracted_text, user_question):
    system_prompt = "You are a helpful technical support assistant. Explain clearly and provide step-by-step guidance."
    user_content = f"""Image content:
{extracted_text if extracted_text else "No visible text detected."}

User question:
{user_question}
"""

    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
        "temperature": 0.3,
        "max_tokens": 512,
    }

    resp = requests.post(f"{BASE_URL}/chat/completions", headers=headers, json=payload, timeout=60)
    if resp.status_code != 200:
        raise RuntimeError(f"NVIDIA API Error {resp.status_code}: {resp.text}")

    data = resp.json()
    return data["choices"][0]["message"]["content"]
