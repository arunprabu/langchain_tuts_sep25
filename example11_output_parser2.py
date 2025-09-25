'''
  An example of using StructuredOutputParser with ChatOpenAI.
  This example demonstrates how to use a StructuredOutputParser to extract specific fields
  from text using a language model.
'''
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
import os
from dotenv import load_dotenv
load_dotenv()

def structured_parser_example():
    llm = ChatOpenAI(model="gpt-5-nano", temperature=0)
    
    response_schemas = [
        ResponseSchema(name="summary", description="brief summary of the text"),
        ResponseSchema(name="sentiment", description="positive, negative, or neutral"),
        ResponseSchema(name="keywords", description="main keywords separated by commas")
    ]
    
    parser = StructuredOutputParser.from_response_schemas(response_schemas)
    
    prompt = PromptTemplate.from_template(
        "Analyze this text: {text}\n{format_instructions}"
    ).partial(format_instructions=parser.get_format_instructions())
    
    chain = prompt | llm | parser
    
    while True:
        text = input("Enter text to analyze (or 'exit'): ").strip()
        if text.lower() == 'exit':
            break
            
        try:
            result = chain.invoke({"text": text})
            print("Analysis Result:")
            print(f"Summary: {result['summary']}")
            print(f"Sentiment: {result['sentiment']}")
            print(f"Keywords: {result['keywords']}")
            print()
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    structured_parser_example()
