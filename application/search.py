from langchain.agents import ZeroShotAgent, Tool, AgentExecutor
from langchain import OpenAI, SerpAPIWrapper, LLMChain


def search(input: str):
    searchh = SerpAPIWrapper()
    tools = [
        Tool(
            name="Search",
            func=searchh.run,
            description="useful for when you need to answer questions about current events"
        )
    ]

    prefix = """Answer the following questions as best and long in german as you can, answering in lawyer speak. You have access to the following tools:"""
    suffix = """Begin! Remember to speak as a business lawyer data protection site when giving your final answer."

    Question: {input}
    {agent_scratchpad}"""

    prompt = ZeroShotAgent.create_prompt(
        tools,
        prefix=prefix,
        suffix=suffix,
        input_variables=["input", "agent_scratchpad"]
    )
    llm_chain = LLMChain(llm=OpenAI(temperature=0), prompt=prompt)
    agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools)
    agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)
    return agent_executor.run(input)
