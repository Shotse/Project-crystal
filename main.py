from agent.brain import chat_with_tools
import sys
sys.stdout.reconfigure(encoding="utf-8")
sys.stdin.reconfigure(encoding="utf-8")



messages = [
    {
        "role": "system",
        "content": """Ты — Crystal. Отвечай по-русски, коротко и по делу. Доступные функции:
    - getcurrenttime() — узнать текущее время в Москве.
    - opencalculator() — открыть калькулятор.
    - click(x, y) — кликнуть мышью по координатам.
    - type_text(text) — ввести текст с клавиатуры.
    - press_key(key) — нажать клавишу.
    - move_mouse(x, y) — переместить мышь.
    - scroll(amount) — прокрутить колесо мыши.
    - screenshot(filename) — сделать скриншот и сохранить в файл.
    - getscreensize() — узнать размер экрана.

    Правила использования:
    - Используй только имена функций из списка.
    - Если нужен аргумент, передавай его явно.
    - Если функция не нужна — отвечай текстом без вызова инструментов.
    Если ты вызвала функцию, то после получения результата отвечай пользователю только обычным человеческим текстом.
    Не показывай JSON, не показывай tool_calls, не показывай названия функций.
    Формулируй ответ коротко и естественно.

    """
    }
]

while True:
    user_input = input("Ты: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Выход из программы.")
        break

    messages.append({"role": "user", "content": user_input})
    answer = chat_with_tools(messages)
    print("Crystal:", answer)
    messages.append({"role": "assistant", "content": answer})


 