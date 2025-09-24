'''
  Interactive Chat with the Assistant -- in Terminal / Command Prompt
'''
from langchain_openai import ChatOpenAI
import os 

from dotenv import load_dotenv
load_dotenv()

def chat_with_assistant(): 
  # Initialize the ChatOpenAI model
  llm = ChatOpenAI(model="gpt-5-mini", temperature=0)
  print("Start Typing with the Assistant")

  while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
      print("Exiting the chat. Goodbye!")
      break

    messages = [
      ("system", "You are a helpful assistant"),
      ("user", user_input)
    ]

    response = llm.invoke(messages)  
    print("Assistant: ", response.content) #this will print only the content of the response

if __name__ == "__main__":
  chat_with_assistant()




