from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()

# Define a Pydantic model for structured output
# Expected example structured data format: {"name": "John Doe", "age": 30, "occupation": "Engineer"}
class PersonInfo(BaseModel):
    name: str = Field(description="person's full name")
    age: int = Field(description="person's age in years")
    occupation: str = Field(description="person's job or profession")

# Example usage of output parsers
def output_parser_example():
    llm = ChatOpenAI(model="gpt-5-nano", temperature=0)
    
    # Method 1: JSON Output Parser with Pydantic
    json_parser = JsonOutputParser(pydantic_object=PersonInfo)
    
    json_prompt = PromptTemplate.from_template(
        "Extract person information from this text: {text}\n{format_instructions}"
    ).partial(format_instructions=json_parser.get_format_instructions())
    
    json_chain = json_prompt | llm | json_parser
    
    # Method 2: Structured Output Parser
    response_schemas = [
        ResponseSchema(name="summary", description="brief summary of the text"),
        ResponseSchema(name="sentiment", description="positive, negative, or neutral"),
        ResponseSchema(name="keywords", description="main keywords separated by commas")
    ]
    
    structured_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    
    structured_prompt = PromptTemplate.from_template(
        "Analyze this text: {text}\n{format_instructions}"
    ).partial(format_instructions=structured_parser.get_format_instructions())
    
    structured_chain = structured_prompt | llm | structured_parser
    
    while True:
        choice = input("Choose parser (1=Person Info, 2=Text Analysis, exit): ").strip()
        if choice.lower() == 'exit':
            break
            
        text = input("Enter text to analyze: ").strip()
        if text.lower() == 'exit':
            break
            
        try:
            if choice == "1":
                result = json_chain.invoke({"text": text})
                print("Parsed Person Info:")
                print(f"Name: {result['name']}")
                print(f"Age: {result['age']}")
                print(f"Occupation: {result['occupation']}")
            elif choice == "2":
                result = structured_chain.invoke({"text": text})
                print("Analysis Result:")
                print(f"Summary: {result['summary']}")
                print(f"Sentiment: {result['sentiment']}")
                print(f"Keywords: {result['keywords']}")
            else:
                print("Invalid choice")
                
            print()
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    output_parser_example()
