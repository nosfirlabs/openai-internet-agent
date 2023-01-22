import os

from application import search

os.environ["OPENAI_API_KEY"] = ""
os.environ["SERPAPI_API_KEY"] = ""
os.environ["INTERNET_AGENT_VERSION"] = "1.0.0"

if __name__ == "__main__":
    # check if env key is set
    if os.environ.get("OPENAI_API_KEY") is None:
        raise ValueError("OPENAI_API_KEY not set")

    # check if env key is empty
    if os.environ.get("OPENAI_API_KEY") == "":
        raise ValueError("OPENAI_API_KEY is empty")
    else:
        print("OPENAI_API_KEY [is set]")
        print("Internet Agent v" + os.environ.get("INTERNET_AGENT_VERSION"))

        while True:
            query = input("Enter your query: ")
            if query == "exit":
                break
            else:
                # try search
                response = search.search(query)
                print("Response: " + str(response))
