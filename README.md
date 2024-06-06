# About
A small example (holiday planning in Split, Croatia) that shows how [CrewAI](https://www.crewai.com) can be used for agentic AI applications. It shows how it is possible to plan a simple holiday.
The system is made of two agents:
* one looks for flights and accomodations in Split, Croatia
* one looks for activities and things to see in Split, Croatia

# Requirements
* [gpt4all](https://gpt4all.io/index.html), in particular you will need to download the embedding model **nomic-ai/nomic-embed-text-v1.5-GGUF**
* [ollama](https://ollama.com), in particular you will need to download the LLM **mistral**
* install the required python libraries by issuing the command **pip install -r requirements.txt**
* get an api key from the [SERPER](https://serper.dev) service, you will need it to set the environment variable **SERPER_AI_KEY** in **run.sh**

# Run the example
Just run the **run.sh** script

**IMPORTANT**: be sure to set the **SERPER_API_KEY**

# Using OpenAI models
The example uses local LLM and embedding models, it is possible to use the OpenAI models via api. Be sure to set the environment variable **OPENAI_API_KEY** and change the code accordingly so that no ollama/gpt4all models are used
