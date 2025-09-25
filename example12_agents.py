from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import tool
import os
from dotenv import load_dotenv
load_dotenv()

@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions. Input should be a valid math expression like '2+2' or '10*5'"""
    try:
        result = eval(expression)
        return f"The result is: {result}"
    except:
        return "Invalid mathematical expression"

@tool
def text_length(text: str) -> str:
    """Count the number of characters in a text string"""
    return f"The text has {len(text)} characters"

def simple_agent_example():
    # MUST USE A MORE CAPABLE MODEL LIKE GPT-5 FOR AGENT TASKS
    llm = ChatOpenAI(model="gpt-5", temperature=0)
    
    # Define available tools
    tools = [calculator, text_length]
    
    # Create agent prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant with access to tools. Use them when needed."),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ])
    
    # Create agent
    agent = create_openai_functions_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    print("Agent with Calculator and Text Length tools ready!")
    print("Try: 'What is 15 * 7?' or 'How many characters in hello world?'")
    
    while True:
        user_input = input("Ask me something (or 'exit'): ").strip()
        if user_input.lower() == 'exit':
            break
            
        try:
            response = agent_executor.invoke({"input": user_input})
            print("Agent:", response["output"])
            print()
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    simple_agent_example()
