import requests
import json
import os

OLLAMA_URL = "http://localhost:11434/api/chat"
HISTORY_FILE = "history.json"
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

conversation_history = load_history()

def chat_with_qwen(user_message):
    conversation_history.append({"role": "user", "content": user_message})
    
    payload = {
        "model": "qwen2.5:1.5b",
        "messages": conversation_history,
        "stream": False
    }
    
    response = requests.post(OLLAMA_URL, json=payload)
    data = response.json()
    reply = data["message"]["content"]
    
    conversation_history.append({"role": "assistant", "content": reply})
    save_history(conversation_history)
    
    return reply

print("Chatbot with persistent memory! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        break
    
    reply = chat_with_qwen(user_input)
    print("Qwen:", reply)
    print()        