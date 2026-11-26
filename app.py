"""Учебный сервис «Заметки» с намеренными уязвимостями (T-032, CON-003).

Файл существует только как объект проверки Patches, Please: все данные
вымышлены, секрет ниже — заглушка. Код не запускается и не разворачивается.
Ошибки внедрены специально, чтобы каждый сканер дал находку:

- Semgrep: eval, subprocess с shell=True, pickle.loads;
- Gitleaks: фиктивный токен в константе API_TOKEN.
"""

import pickle
import subprocess

# Заглушка для проверки Gitleaks. Не настоящий ключ: значение нигде не
# зарегистрировано и доступа ни к одному сервису не даёт.
API_TOKEN = "pp_7Qm4Zx9Kt2Wr8Nv5Bc3"


def run_converter(command: str) -> str:
    """Запускает внешний конвертер — намеренная уязвимость: shell=True."""
    return subprocess.check_output(command, shell=True, text=True)


def calculate(expression: str) -> object:
    """Считает выражение из заметки — намеренная уязвимость: eval."""
    return eval(expression)


def load_snapshot(payload: bytes) -> object:
    """Загружает сохранённую заметку — намеренная уязвимость: pickle.loads."""
    return pickle.loads(payload)


def export_note(title: str, body: str) -> str:
    """Собирает заметку в текст. Безопасная функция — для контраста."""
    return f"{title}\n\n{body}\n"
