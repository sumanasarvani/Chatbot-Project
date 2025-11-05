from openai import OpenAI
import os
from dotenv import load_dotenv

# Loading the environment from the .env file
load_dotenv()

# Intializing the client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.environ["NVIDIA_API_KEY"]
)

# Initialize chat history
conversation_history = [
    {
        "role": "system", "content": "You are a helpful and friendly chatbot."
    }
]

def chat_with_gpt(user_input):
    # Adding user's message to the conversation memory
    conversation_history.append({
        "role": "user", "content": user_input
    })
    
    # Sending the entire conversation to the model
    response = client.chat.completions.create(
        model="deepseek-ai/deepseek-v3.1",
        messages=conversation_history
    )
    
    # Getting a reply from the assistant
    reply = response.choices[0].message.content.strip()
    
    # Adding the assistant's reply to the memory
    conversation_history.append({
        "role": "assistant", "content": reply
    })
    
    return reply

if __name__ == "__main__":
    print("Chatbot: Hello! Type 'exit' or 'quit' or 'bye' to end the chat.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
          print("Goodbye!")
          break
      
        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
            