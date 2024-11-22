
import os
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.tools import searchapi
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import pprint
from langchain.agents import create_tool_calling_agent , AgentExecutor
from dotenv import load_dotenv
load_dotenv()


serper_api_key= os.getenv("SERPER_API_KEY")

search = GoogleSerperAPIWrapper()

# print(search.run("Obama's first name?"))

tools= [search]

prompt = PromptTemplate.from_template(
    """
    You are the helpful assistant that answers the questions based on the search results.
    To answer question, you can use the following tools:
    - Google Search: Search Google for accurate information.
    Question : {query}

    {agent_scratchpad}
"""
)

llm = ChatGroq(model_name ="llama3-groq-70b-8192-tool-use-preview")

agent = create_tool_calling_agent(llm,tools,prompt)


agent_executor = AgentExecutor(
    agent= agent, tools=tools,
    verbose = True
)

response = agent_executor.invoke({
    "query" : "Tell me about something about Elon musk"
})

print("FinalResponse", response)