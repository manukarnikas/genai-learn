import ollama

stream = ollama.chat(
    model="tinyllama",
    messages=[
        {'role':'system','content': 'you are helpful assistant'},
        {'role':'user','content': 'what is ollama'}
    ],
    stream = true
)

for chunk in stream:
    print(chunk['message']['content'],end='',flush = true)

