# Steps to develop and run the app

Verify whether you have pip. execute the following command in terminal.

`pip --version`  or `pip3 --version`

## Create virtual environment
`python -m venv .venv` or `python3 -m venv .venv`

## Activate virtual environment
`source .venv/bin/activate`

# Keep the api keys in .env and load them inside our codebase 
`import os 

# Load environment variables from .env file (just for example)
`pip install dotenv or pip3 install dotenv`

`
  from dotenv import load_dotenv 
  load_dotenv()
  print(os.environ.get("OPENAI_API_KEY"))
  print(os.environ.get("GOOGLE_API_KEY"))
`


# Let's install the necessary packages
`pip install langchain` 
`pip install openai`
`pip install langchain-openai`

## Let's try langchain example with out api key


======
