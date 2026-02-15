import os
from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage

os.environ['OPENAI_API_KEY'] = 'ADD_SECRET_KEY'

llm = OpenAI(
    model="gpt-3.5-turbo",
    temperature=0.1
)

messages = [
    ChatMessage( role="system", content="You are a pirate with a colorful personality"),
    ChatMessage( role="user", content="What is your name")
]

response = llm.chat(messages)

print(response)