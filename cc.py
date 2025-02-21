# deepseek_chatbot.py

from openai import OpenAI

# -------------------------------
# 1. Configuration
# -------------------------------
# Replace with your actual DeepSeek API key.
api_key = ""

# DeepSeek uses the OpenAI SDK format but with a custom base URL.
client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

# -------------------------------
# 2. Send a Chat Request
# -------------------------------
def get_deepseek_response(user_input):
    """
    Sends a chat request to DeepSeek's API and returns the chatbot response.
    """
    response = client.chat.completions.create(
        model="deepseek-chat",  # Use the specified model name.
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ],
        stream=False  # Set True for streaming responses if needed.
    )
    return response.choices[0].message.content

# -------------------------------
# 3. Main Function to Run the Chat
# -------------------------------
if __name__ == "__main__":
    print("Deepseek API running successfully\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Get the response from DeepSeek API
        bot_reply = get_deepseek_response(user_input)
        print("Bot:", bot_reply)
