
# AI Agents
---
  Python, JavaScript (Vercel AI SDK, Langchain JS), DotNet (SemanticKernel)

## AI Agent Development Frameworks
---
  ### Python-based 
  ----
    1. LangChain (also available as JS package)
    2. CrewAI
    3. LlamaIndex
    4. Agno



## LangChain 
===

### Core Building Blocks of AI agents
---
  1. LLM with Reasoning Capability / LLM tuned for AI Agents
  2. Prompts  (preferred: ReAct)
  3. Tools / Functions / Integrations / MCP (WebSearch, Weather)
  4. Knowledge Base (optional)
  5. Memory (third party tools)
  6. Guardrails (third party tools)
  7. Observability (Evaluate AI Agent)

=====

## Components of Langchain 
1. Chat models [DONE]
2. Messages [DONE]
3. Prompt templates [DONE]
4. Example selectors
5. LLMs [DONE]
6. Output parsers [DONE]
7. Document loaders
8. Text splitters
9. Embedding models
10. Vector stores
11. Retrievers 
12. Tools [TODO]
13. Agents [TODO]
14. Multimodal
15. Indexing 


Agents
===
  Requirement 
    * our agent listens to users queries related to weather and answers 
    * should we address queries outside the original scope? no 

Tools 
===
  * simple function that does something 
  * must have name and description [this needs to have clarity] properties 
  * must return value
  * description is a prompt for the tool 
  * function arguments are optional


