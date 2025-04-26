# Import the necessary library
import google.generativeai as genai

# --- Configuration ---
# WARNING: Hardcoding API keys is insecure. Revoke this key.
API_KEY = "AIzaSyBIVkeXW7JpZzQxJZY72ZlO0lHxFYEpuMk"


# Configure the library with the API key
genai.configure(api_key=API_KEY)

# Select the model (gemini-1.5-flash is often in the free tier)
model = genai.GenerativeModel('gemini-1.5-flash')

# Start a chat session
chat = model.start_chat(history=[])

print("Chatting with Gemini (type 'quit' to exit)...")

# Simple chat loop
while (prompt := input("You: ").strip()) != 'quit':
    response = chat.send_message(prompt)
    print(f"Gemini: {response.text}")

print("Chat ended.")

