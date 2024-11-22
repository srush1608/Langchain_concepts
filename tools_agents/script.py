from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

# search= TavilySearchResults()
search= DuckDuckGoSearchRun()

# can call multiple tools
tools = [search]

prompt =PromptTemplate.from_template(
    """
You are helpful assistant that answers questions based on search results.
To answer question , you can use the following tools:
duckduckgo_search_run : Search the web for information

Question : {query}

{agent_scratchpad}
"""
)

# llm= ChatGroq(model_name="llama3-70b-8192")
# llm= ChatGroq(model_name="llama3-groq-70b-8192-tool-use-preview")
llm= ChatGroq(model_name="llama-3.1-70b-versatile")


# agent read prompt----- tools---agent scratchpad---again send to llm ----call tool/not llm decide and last give response

agent = create_tool_calling_agent(llm,tools,prompt)     

# print(search.invoke("Tell me something about Elon musk"))
# ceated agent
agent_executor = AgentExecutor(
    agent=agent,tools=tools,
    verbose=True,
    # max_execution_time=1,--------> Final Response: {'query': ' Tell me something about Elon Musk', 'output': 'Agent stopped due to max iterations.'}    
)

response = agent_executor.invoke({
    "query":" Tell me something about Elon Musk"
})

print("Final Response:",response)
