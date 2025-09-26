from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from dotenv import load_dotenv
load_dotenv()

def document_processing_example():
    llm = ChatOpenAI(model="gpt-5-nano", temperature=0)
    
    # Create a sample text file if it doesn't exist
    sample_text = """
    Python is a high-level programming language known for its simplicity and readability.
    It was created by Guido van Rossum and first released in 1991. Python supports
    multiple programming paradigms including procedural, object-oriented, and functional
    programming. It has a large standard library and an active community that contributes
    to its ecosystem. Python is widely used in web development, data science, artificial
    intelligence, automation, and many other fields.
    """
    
    with open("sample.txt", "w") as f:
        f.write(sample_text)
    
    # Load document
    loader = TextLoader("sample.txt")
    document = loader.load()
    
    # Split document into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20
    )
    chunks = text_splitter.split_documents(document)
    
    # Create prompt template for document analysis
    template = PromptTemplate.from_template(
        "Analyze this text and {task}: {text}"
    )
    
    chain = template | llm
    
    # Interactive processing
    while True:
        task = input("What should I do with the document? (summarize/extract keywords/exit): ").strip()
        if task.lower() == 'exit':
            break
            
        try:
            for i, chunk in enumerate(chunks):
                print(f"Processing chunk {i+1}:")
                response = chain.invoke({
                    "task": task,
                    "text": chunk.page_content
                })
                print(response.content)
                print("-" * 30)
                
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    document_processing_example()
