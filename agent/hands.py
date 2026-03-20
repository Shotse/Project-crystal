from datetime import datetime
from zoneinfo import ZoneInfo
import subprocess
import pyautogui

def getcurrenttime():
    tz = ZoneInfo("Europe/Moscow")
    now = datetime.now(tz)
    return now.strftime("%H:%M")

def opencalculator():
    try:
        subprocess.Popen('calc.exe')
        return "Калькулятор открыт."
    except Exception as e:
        return f"Не удалось открыть калькулятор: {e}"
    
def click(x, y):
    try:
        pyautogui.click(x, y)
        return f"Клик выполнен по координатам ({x}, {y})."
    except Exception as e:
        return f"Не удалось выполнить клик: {e}"

def type_text(text):
    try:
        pyautogui.typewrite(text)
        return f"Текст '{text}' введён."
    except Exception as e:
        return f"Не удалось ввести текст: {e}"
    
def press_key(key):
    try:
        pyautogui.press(key)
        return f"Клавиша '{key}' нажата."
    except Exception as e:
        return f"Не удалось нажать клавишу: {e}"

def move_mouse(x, y):
    try:
        pyautogui.moveTo(x, y)
        return f"Мышь перемещена к координатам ({x}, {y})."
    except Exception as e:
        return f"Не удалось переместить мышь: {e}"

def scroll(amount):
    try:
        pyautogui.scroll(amount)
        return f"Прокрутка выполнена на {amount} единиц."
    except Exception as e:
        return f"Не удалось выполнить прокрутку: {e}"

def screenshot(filename):
    try:
        pyautogui.screenshot(filename)
        return f"Скриншот сохранён как '{filename}'."
    except Exception as e:
        return f"Не удалось сделать скриншот: {e}"

def getscreensize():
    try:
        width, height = pyautogui.size()
        return f"Размер экрана: {width}x{height}."
    except Exception as e:
        return f"Не удалось получить размер экрана: {e}"