import ollama

response = ollama.chat(
    model="tinyllama",
    messages=[
        {'role':'system','content': 'you are helpful assistant'},
        {'role':'user','content': 'what is ollama'}
    ]
)

print(response['message']['content'])