from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os 
from dotenv import load_dotenv

load_dotenv()

def simple_prompt_template_example():
    llm = ChatOpenAI(model="gpt-5-nano", temperature=0)
    
    prompt_template = PromptTemplate.from_template(
        "Write a short joke about {topic} that is {style}."
    )
    
    # let's see the template details
    # print("Template:", prompt_template.template)
    # print("Variables:", prompt_template.input_variables)

    chain = prompt_template | llm

    # Interactive user input loop
    print("Welcome to the Joke Generator!")
    print("Type 'exit' to quit\n")
    
    while True:
        try:
            topic = input("Topic: ").strip()
            if topic.lower() == 'exit':
                break
                
            style = input("Style: ").strip()
            if style.lower() == 'exit':
                break
            
            response = chain.invoke({"topic": topic, "style": style})
            print(response.content)
            print()

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    simple_prompt_template_example()
