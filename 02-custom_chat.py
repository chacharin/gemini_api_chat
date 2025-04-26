import google.generativeai as genai

# --- Configuration ---
API_KEY = "AIzaSyBIVkeXW7JpZzQxJZY72ZlO0lHxFYEpuMk" # <<< --- Still using the exposed key
SYSTEM_INSTRUCTION = "คุณเป็นสุดยอดเกษตรกรที่มีความสามารถมากในการปลูกพืชผักสวนครัว โปรดให้คำแนะนำฉันเป็นภาษาไทย"
GENERATION_CONFIG =  {"temperature": 0.7}

# Configure the library with the API key
genai.configure(api_key=API_KEY)

# --- Model Initialization with System Instruction ---
# Select the model and apply the system instruction
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction=SYSTEM_INSTRUCTION,
    generation_config=GENERATION_CONFIG
)

# Start a chat session (history is maintained automatically)
chat = model.start_chat(history=[])

print(f"Chatting with Gemini (Role: {SYSTEM_INSTRUCTION})")
print("Type 'quit' to exit...")
print("-" * 20) # Separator for clarity

# Simple chat loop
while (prompt := input("You: ").strip().lower()) != 'quit': # Convert to lowercase for quit command
    if not prompt: # Skip empty input
        continue
    try:
        # Send the user's message to the chat session
        response = chat.send_message(prompt)
        # Print the model's response text
        print(f"Gemini: {response.text}")
    except Exception as chat_error:
        # Handle potential errors during message sending (e.g., network issues, content filtering)
        print(f"\nError sending message: {chat_error}")
        print("Please try again.")
    print("-" * 20) # Separator for clarity

print("\nChat ended.")



