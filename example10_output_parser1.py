'''
    This example demonstrates how to use a JSON output parser with a Pydantic model
    to extract structured information from text using a language model.
'''
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()

# Define a Pydantic model for structured output
# This model represents a person's information in JSON format {"name": str, "age": int, "occupation": str}
class PersonInfo(BaseModel):
    name: str = Field(description="person's full name")
    age: int = Field(description="person's age in years")
    occupation: str = Field(description="person's job or profession")

# Example function to demonstrate JSON output parsing
def json_parser_example():
    llm = ChatOpenAI(model="gpt-5-nano", temperature=0)
    
    parser = JsonOutputParser(pydantic_object=PersonInfo)
    
    prompt = PromptTemplate.from_template(
        "Extract person information from this text: {text}\n{format_instructions}"
    ).partial(format_instructions=parser.get_format_instructions())
    
    chain = prompt | llm | parser
    
    while True:
        text = input("Enter text with person info (or 'exit'): ").strip()
        if text.lower() == 'exit':
            break
            
        try:
            result = chain.invoke({"text": text})
            print("Parsed JSON:")
            print(f"Name: {result['name']}")
            print(f"Age: {result['age']}")
            print(f"Occupation: {result['occupation']}")
            print()
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    json_parser_example()
