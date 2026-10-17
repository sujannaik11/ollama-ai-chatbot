
from ollama import Client

# 1. Initialize the Ollama client
client = Client(host="http://localhost:11434")

# 2. Store conversation history
messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful AI assistant. "
            "Keep your answers simple, clear, and informative. "
            "Do not use bullet points or numbering."
        )
    }
]

print("Welcome to Ollama AI Chatbot!")
print("Type 'exit' to stop chatting.\n")

# 3. Start an interactive conversation
while True:
    question = input("You: ")

    if question.lower().strip() == "exit":
        print("AI: Goodbye! Have a great day!")
        break

    if not question.strip():
        continue

    # Add user message to conversation history
    messages.append({
        "role": "user",
        "content": question
    })

    # 4. Generate AI response
    completion = client.chat(
        model="qwen3.5:0.8b",
        messages=messages,
        think=False,
        options={
            "temperature": 0.7
        }
    )

    # 5. Extract the AI response
    answer = completion.message.content.strip()

    # 6. Display the AI response
    print("\nAI:", answer, "\n")

    # 7. Save AI response to conversation history
    messages.append({
        "role": "assistant",
        "content": answer
    })
