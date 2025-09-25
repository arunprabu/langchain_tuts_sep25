'''
  Chat with Memory+ System Prompt + Prompt Template -- in Terminal / Command Prompt
'''
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
import os 

from dotenv import load_dotenv
load_dotenv()

def chat_with_memory():
    llm = ChatOpenAI(model="gpt-5-mini", temperature=0)
    memory = ConversationBufferMemory(return_messages=True)
    
    # Create a system prompt for shorter responses
    system_prompt = PromptTemplate(
        input_variables=["history", "input"],
        template="""You are a helpful AI assistant. Please keep your 
        responses concise and to the point. 
        Aim for brief, clear answers without unnecessary elaboration.

        Previous conversation:
        {history}

        Current input: {input}

        Please provide a brief and helpful response:"""
    )
    
    conversation = ConversationChain(
        llm=llm, 
        memory=memory,
        prompt=system_prompt
    )

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
            # --- Debug: Print the memory buffer here ---
            print('--- Conversation History ---')
            print(memory.buffer)  # For plain string history
            # or, for formatted variable history:
            print(memory.load_memory_variables({})["history"])
            print('----------------------------')


        except Exception as e:
            print("Oops! Something went wrong:", e)

if __name__ == "__main__":
    chat_with_memory()


"""
    Here's the Prompt to test this

    You: I watched interstellar recently
    Assistant: 

    You: list down most popular programming languages
    Assistant: 

    You: what movie i watched?
    Assistant: Interstellar

"""
