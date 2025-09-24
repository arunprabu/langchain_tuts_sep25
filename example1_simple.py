'''
  verisons used here 
  langchain==0.3.27
  langchain_openai==0.3.33
'''
from langchain_openai import ChatOpenAI
import os 

# Load environment variables from .env file
from dotenv import load_dotenv #pip install dotenv or pip3 install dotenv
load_dotenv()

def main(): 
  # Initialize the ChatOpenAI model
  llm = ChatOpenAI(model="gpt-5-mini", temperature=0)

  messages = [
    ("system", "You are a helpful assistant"), # system prompt
    ("user", "Hello")
  ]

  response = llm.invoke(messages)
  # print(response) #this will print json output
  print("Assistant: ", response.content) #this will print only the content of the response
  # print(response.text()) #this will print only the content of the response

if __name__ == "__main__":
  main()




