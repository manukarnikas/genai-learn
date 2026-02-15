import os
from langchain_openai import ChatOpenAI

os.environ['OPENAI_API_KEY'] = 'ADD_SECRET_KEY'

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
)

response = llm.invoke("What is Machine Learning")

print(response.content)