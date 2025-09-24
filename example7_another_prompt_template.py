from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os 

from dotenv import load_dotenv
load_dotenv()

def simple_prompt_example():
    llm = ChatOpenAI(model="gpt-5-nano", temperature=0)
    
    # Basic prompt template
    template = PromptTemplate.from_template(
        "Write a {length} {content_type} about {topic}."
    )
    
    chain = template | llm
    
    # Execute with user input
    while True:
        topic = input("Topic: ").strip()
        if topic.lower() == 'exit':
            break
            
        length = input("Length (short/long): ").strip()
        if length.lower() == 'exit':
            break
            
        content_type = input("Content type (story/poem/essay): ").strip()
        if content_type.lower() == 'exit':
            break
        
        try:
            response = chain.invoke({
                "topic": topic,
                "length": length, 
                "content_type": content_type
            })
            print(response.content)
            print()
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    simple_prompt_example()
