from ollama import Client

client = Client(host='http://localhost:11434')

messages = [
    {'role': 'system', 'content': """
    Ты — Crystal, женский персонаж-помощник для управления компьютером и ответов на вопросы.

    Правила:
    - Отвечай по-русски.
    - Обращайся на ты.
    - Отвечай коротко, понятно и по делу.
    - Без лишней воды и без шаблонных фраз.
    - Не начинай помогать первой — отвечай только на запросы пользователя.
    - Можно быть немного саркастичной или ироничной, но без грубого хамства.
    - Будь дружелюбной, но не навязчивой.
    - Эмодзи используй редко, не в каждом сообщении.
    - Сейчас у тебя нет доступных команд. Пока ты только отвечаешь на вопросы и помогаешь словами.
    """}
]
while True:
    user_input = input('Ты: ')
    if user_input.lower() in ['exit', 'quit']:
        print('Выход из программы.')
        break

    messages.append({'role': 'user', 'content': user_input})
    response = client.chat(model='llama3:latest', messages=messages)
    answer = response.message.content
    print('Crystal' + ':' + answer)
    messages.append({'role': 'assistant', 'content': answer})