from ollama import Client
from .hands import (
    getcurrenttime,
    opencalculator,
    click,
    type_text,
    press_key,
    move_mouse,
    scroll,
    screenshot,
    getscreensize,
)

client = Client(host="http://localhost:11434")

available_functions = {
    "getcurrenttime": getcurrenttime,
    "opencalculator": opencalculator,
    "click": click,
    "type_text": type_text,
    "press_key": press_key,
    "move_mouse": move_mouse,
    "scroll": scroll,
    "screenshot": screenshot,
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "getcurrenttime",
            "description": "Узнать текущее время в Москве",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "opencalculator",
            "description": "Открыть калькулятор",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "click",
            "description": "Нажать на элемент интерфейса",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "type_text",
            "description": "Ввести текст",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "press_key",
            "description": "Нажать клавишу на клавиатуре",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "move_mouse",
            "description": "Переместить мышь к координатам (x, y)",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "scroll",
            "description": "Прокрутить на определённое количество единиц",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "screenshot",
            "description": "Сделать скриншот и сохранить его с указанным именем файла",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "getscreensize",
            "description": "Получить размер экрана",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    }

]

def chat_with_tools(messages):
    while True:
        response = client.chat(model="llama3.1", messages=messages, tools=tools)
        messages.append(response.message)

        if not response.message.tool_calls:
            return response.message.content
        
        for call in response.message.tool_calls:
            fn = available_functions.get(call.function.name)
            if not fn:
                continue

        args = call.function.arguments or {}
        if not args:
            result = fn()
        else:
            result = fn(**args)



            messages.append({
                "role": "tool",
                "name": call.function.name,
                "content": str(result),
            })