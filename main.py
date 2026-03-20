from ollama import Client
from agent import getcurrenttime, opencalculator

available_functions = {
    "getcurrenttime": getcurrenttime,
    "opencalculator": opencalculator,
}

tools = [getcurrenttime, opencalculator]


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
    - У тебя есть папка agent с командами для управления компьютером, которые ты можешь использовать, если пользователь попросит тебя что-то сделать. Команды:
    - getcurrenttime() — узнать текущее время в Москве.
    - opencalculator() — открыть калькулятор на компьютере.

    """}
]


while True:
    user_input = input('Ты: ')
    if user_input.lower() in ['exit', 'quit']:
        print('Выход из программы.')
        break
    messages.append({'role': 'user', 'content': user_input})

    response = client.chat(model='llama3.1', tools=tools, messages=messages)
    messages.append(response.message)

    if response.message.tool_calls:
        for call in response.message.tool_calls:
            fn = available_functions.get(call.function.name)
            if fn:
                result = fn()
                messages.append({
                    "role": "tool",
                    "name": call.function.name,
                    "content": result
                })

        response = client.chat(model='llama3.1', tools=tools, messages=messages)

    answer = response.message.content
    print("Crystal:", answer)
    messages.append({'role': 'assistant', 'content': answer})
