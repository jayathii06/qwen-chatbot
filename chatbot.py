import requests

OLLAMA_URL = "http://localhost:11434/api/chat"

def chat_with_qwen(user_message):
    payload = {
        "model": "qwen2.5:1.5b",
        "messages": [
            {"role": "user", "content": user_message}
        ],
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    data = response.json()
    return data["message"]["content"]

print("Chatbot ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        break
    
    reply = chat_with_qwen(user_input)
    print("Qwen:", reply)
    print()