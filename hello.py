import requests
import json

# -------------------------------
# 1. Configuration
# -------------------------------
# Replace 'YOUR_API_KEY' with the actual API key you obtained.
API_KEY = "sk-eebb919971484efd98dd36bbe64d69d5"

# Replace the URL with the actual DeepSeek R1 API endpoint.
API_URL = "https://api.deepseek.com"

# -------------------------------
# 2. Define the Chat Function
# -------------------------------
def send_chat_request(user_message):
    """
    Sends a chat message to the DeepSeek R1 API and returns the response.
    
    Parameters:
      user_message (str): The message from the user.
    
    Returns:
      str: The chatbot's response.
    """
    
    # Prepare headers with your API key for authentication.
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    # Prepare the payload.
    # You can customize the 'system' message or add more context.
    payload = {
        "model": "deepseek-r1",  # Specify the model if required
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ],
        "max_tokens": 150  # Adjust based on the desired length of the response
    }
    
    try:
        # Make the POST request to the DeepSeek R1 API.
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        
        # Parse the JSON response.
        data = response.json()
        # Assuming the response structure contains choices with messages,
        # adjust the keys if the actual API returns a different structure.
        bot_reply = data['choices'][0]['message']['content']
        return bot_reply
    
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An error occurred: {err}"

# -------------------------------
# 3. Interactive Chat Loop
# -------------------------------
if __name__ == "__main__":
    print("Welcome to the DeepSeek R1 Chatbot!")
    print("Type your message and press Enter. Type 'exit' to quit.\n")
    
    while True:
        # Get input from the user.
        user_input = input("You: ")
        
        # Check if the user wants to exit.
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat. Goodbye!")
            break
        
        # Send the message to the API and print the bot's response.
        bot_response = send_chat_request(user_input)
        print("Bot:", bot_response)
