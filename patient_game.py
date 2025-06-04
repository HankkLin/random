import os
import requests

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
API_TOKEN = os.environ.get("HF_API_TOKEN")

HEADERS = {"Authorization": f"Bearer {API_TOKEN}"} if API_TOKEN else {}
SYSTEM_PROMPT = (
    "You are a patient experiencing a set of symptoms. "
    "Do not reveal your illness directly. "
    "Answer questions truthfully based on those symptoms."
)


def query_llm(prompt: str) -> str:
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 100}}
    resp = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    if isinstance(data, list) and data:
        text = data[0].get("generated_text", "")
    else:
        text = data.get("generated_text", "")
    return text.strip()


def main() -> None:
    conversation = SYSTEM_PROMPT
    print("LLM Patient Guessing Game")
    print("Type 'quit' to exit.")
    while True:
        question = input("You: ").strip()
        if question.lower() in {"quit", "exit"}:
            break
        prompt = f"{conversation}\nUser: {question}\nPatient:"
        answer = query_llm(prompt)
        print(f"Patient: {answer}")
        conversation = f"{prompt} {answer}"


if __name__ == "__main__":
    main()

