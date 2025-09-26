
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



Types of AI Agents
--
  1. Autonomous 
  2. Semi-Autonomous


Factors to consider when we build AI Agents
---
  1. Does the model have reasoning capability?
  2. Can the model perform the tool calls / function calls
  3. Context window 


====
2 Approaches 
---
  Single Agent with many tools 
    1. get_user_location
    2. get_date
    3. get_weather
    4. get_weather_forecast
    5. book_turf 
    6. make_payment
    7. send_notification_for_otp
    8. get_otp 
    9. send_booking_confirmation
  Many tiny agents with individual tools 
    1. userInfoCollector agent 
        1. get_user_location
        2. get_date
        3. get_weather
        4. get_weather_forecast

    2. bookingAgent 
        1. book_turf 
        2. make_payment
        3. get_otp 

    3. NotifierAgent 
        1. send_notification_for_otp
        2. send_booking_confirmation



