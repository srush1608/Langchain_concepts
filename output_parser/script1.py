from langchain_core.prompts.prompt import PromptTemplate
from langchain_groq.chat_models import ChatGroq

context = """David Jonathan Smith, a 32-year-old male, is a software engineer known for his innovative approach to solving complex technical problems. Born on April 12, 1992, in San Francisco, California, David developed an early interest in computers and technology. He pursued his passion academically, earning a Bachelor's degree in Computer Science from Stanford University in 2014. Later, he completed a Master's in Artificial Intelligence from the Massachusetts Institute of Technology (MIT) in 2017. Professionally, David has built a career specializing in AI and machine learning, working as a senior engineer at a leading tech firm. He has contributed to several groundbreaking projects, including advancements in natural language processing and autonomous systems. His father, Richard Alan Smith, a retired physicist, greatly influenced David's curiosity for science and his methodical approach to problem-solving. In addition to his professional achievements, David enjoys mentoring young coders, often volunteering at community tech workshops. Outside of work, he has a passion for hiking and photography, frequently exploring the scenic landscapes of Northern California. David's dedication to innovation, coupled with his strong academic background and supportive upbringing, has made him a respected figure both in his professional field and his local community."""

# prompt = """
# According to the given context{context}, provide the following details in dictionary:
# {{
#     "name": "<name>",
#     "age": <age>,
#     "gender": "<gender>",
#     "date_of_birth": "<DD-MM-YYYY>",
#     "education": "<education>",
#     "profession": "<profession>"
# }}
# """

prompt = """
According to the given context{context}, provide the following details in JSON format:
{{
    "name": "<name>",
    "age": <age>,
    "gender": "<gender>",
    "date_of_birth": "<DD-MM-YYYY>",
    "education": "<education>",
    "profession": "<profession>"
}}
"""


prompt_template = PromptTemplate(
    template=prompt
)

llm = ChatGroq(
    model_name="llama3-70b-8192",
    groq_api_key="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"
)

chain = prompt_template | llm

response = chain.invoke({"context": context}).content

# parsing here

# Print the response
print(response)
