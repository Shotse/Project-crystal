from datetime import datetime
from zoneinfo import ZoneInfo
import subprocess


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