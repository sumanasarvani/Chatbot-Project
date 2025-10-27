from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = os.environ["NVIDIA_API_KEY"]
)
def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model = "deepseek-ai/deepseek-v3.1",
        messages = [{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        
        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
        
