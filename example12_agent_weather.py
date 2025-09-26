from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import tool
import requests # rest api client
import json # json parsing
import os
from dotenv import load_dotenv
load_dotenv()

@tool
def weather_tool1(location: str) -> str:
    # description of the tool
    """get the current weather at a location"""
    try:
        API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
        
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=60)
        data = response.json()
        
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        
        return f"{location}: {temp}°C, {description}"
        
    except Exception as e:
        return f"Error: {str(e)}"
    


# here comes our agent
def simple_weather_agent():
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    
    tools = [weather_tool ]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a weather assistant.
         You have access to some tools. Make use of them."""),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ])
    
    agent = create_openai_functions_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    print("🌤️ Weather Agent")
    
    while True:
        city = input("Enter city name (or 'exit'): ").strip()
        if city.lower() == 'exit':
            break
            
        try:
            response = agent_executor.invoke({"input": f"Get weather for {city}"})
            print(response["output"])
            print("-" * 40)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    simple_weather_agent()
