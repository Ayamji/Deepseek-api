import requests
import json


API_KEY = "xxx"


API_URL = "https://api.deepseek.com"



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
    
 .
    payload = {
        "model": "deepseek-r1",  
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ],
        "max_tokens": 150 
    }
    
    try:
       
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  
        
       
        data = response.json()
      
        bot_reply = data['choices'][0]['message']['content']
        return bot_reply
    
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An error occurred: {err}"


if __name__ == "__main__":
    print("Welcome to the DeepSeek R1 Chatbot!")
    print("Type your message and press Enter. Type 'exit' to quit.\n")
    
    while True:
     
        user_input = input("You: ")
        
       
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat. Goodbye!")
            break
        
        bot_response = send_chat_request(user_input)
        print("Bot:", bot_response)
