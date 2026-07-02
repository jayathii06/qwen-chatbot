import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
conversation_history = []

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
    
    return reply


print("Chatbot with memory! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        break
    
    reply = chat_with_qwen(user_input)
    print("Qwen:", reply)
    print()