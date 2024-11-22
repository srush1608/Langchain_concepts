from langchain import hub
import os
from langchain.agents import AgentExecutor, create_react_agent
# from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import Tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

search = GoogleSerperAPIWrapper()


tools = [
    Tool(
        name="Intermediate Answer",
        func=search.run,
        description="useful for when you need to ask with search",
    )
]
# Get the prompt to use - you can modify this!
prompt = hub.pull("hwchase17/react")

# Choose the LLM to use
llm = ChatGroq()
# llm = ChatGroq(temperature=0.3)

agent = create_react_agent(llm,tools,prompt)
agent_executor = AgentExecutor(
    agent= agent, tools=tools,
    verbose = True
)

response = agent_executor.invoke({
    "input" : "Tell me about something about Elon musk"
})


print("FinalResponse", response)