
# Internet Agent

This is an internet search agent that uses the OpenAI API and SERP API to search the internet and return relevant results.

Build using `LangChain`: [Repo](https://github.com/hwchase17/langchain)

## Requirements

-   An API key for the OpenAI API
-   An API key for the SERP API

## Usage

1.  Set the API keys as environment variables. The variable names should be "OPENAI_API_KEY" for the OpenAI API key, and "SERPAPI_API_KEY" for the SERP API key.

`export OPENAI_API_KEY=your_openai_api_key`

`export SERPAPI_API_KEY=your_serp_api_key` 

2.  Run the main script:

`python main.py` 

3.  The script will prompt you to enter a query. Type in your query and press enter.
    
4.  The script will return a response containing the relevant search results.
    
5.  To exit the program, type "exit" when prompted for a query.
    

## Note

-   This is a sample code for reference, OpenAI and SERPAPI are paid services so you will need to sign up for their services and generate your own API key to use it.
    
-   You may need to install additional modules or packages to run the script.
    
-   The version of the internet agent is set in the environment variable "INTERNET_AGENT_VERSION".
    
-   The OpenAI and SERP API keys are read from the environment variables "OPENAI_API_KEY" and "SERPAPI_API_KEY", respectively.
