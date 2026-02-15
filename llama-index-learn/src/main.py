import os
from llama_index.llms.openai import OpenAI

os.environ['OPENAI_API_KEY'] = 'ADD_SECRET_KEY'
llm = OpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
)

response = llm.complete(" Machine Learning is")

print(response)