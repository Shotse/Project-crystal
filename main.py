from ollama import Client

client = Client(host='http://localhost:11434')

response = client.chat(
    model='llama3:latest',
    messages=[
        {'role': 'system', 'content': 'Ты полезный ассистент.'},
        {'role': 'user', 'content': 'Скажи привет одной короткой фразой.'}
    ]
)

print(response.message.content)
