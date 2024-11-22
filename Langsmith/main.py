from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

# llm = ChatGroq(model_name ="llama3-groq-70b-8192-tool-use-preview")


# print(llm.invoke("What is capital of India").content)
prompt = PromptTemplate(
    template=""""
    context:
    {context}
    question:
    {question}
    """
)

llm = ChatGroq(model_name ="llama3-groq-70b-8192-tool-use-preview")

chain = {
    "context":lambda  x : x["context"],
    "question":lambda x: x["question"]
} | prompt |llm

print(chain.invoke({"context" : " New Delhi is capital of India","question":"what is capitial of India"}).content)