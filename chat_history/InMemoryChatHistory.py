from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq.chat_models import ChatGroq


chat_history = InMemoryChatMessageHistory()


system_prompt = """You are a health expert. Your objective is to help the user with their health issues. Respond in text only."""
chat_history.add_messages(SystemMessage(content=system_prompt))
human_prompt = """Hey, I am John. I am 23 year old."""
chat_history.add_messages(HumanMessage(content=human_prompt))

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", human_prompt)
])

llm = ChatGroq(
    model_name="llama3-70b-8192",
    groq_api_key="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"
)

chain = chat_prompt | llm

response = chain.invoke({}).content
chat_history.add_messages(AIMessage(content=response))


print(chat_history.messages)
print(response)