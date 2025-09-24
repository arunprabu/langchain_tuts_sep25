'''
  Chat with Memory using LangChain and OpenAI -- in Terminal / Command Prompt
'''
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os 

from dotenv import load_dotenv
load_dotenv()

def chat_with_memory():
    llm = ChatOpenAI(model="gpt-5-mini", temperature=0)
    memory = ConversationBufferMemory(return_messages=True)
    conversation = ConversationChain(llm=llm, memory=memory)

    print("Chat with memory enabled! (Type 'exit' to quit)")

    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            # Use invoke instead of run for newer LangChain versions
            response = conversation.invoke({"input": user_input})
            print("Assistant:", response['response'])

        except Exception as e:
            print("Oops! Something went wrong:", e)

if __name__ == "__main__":
    chat_with_memory()

