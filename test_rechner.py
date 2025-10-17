import time
import pytest
import pyautogui
import subprocess
import pyperclip

@pytest.fixture(scope="module")
def start_calculator():
    #Запускает Калькулятор Windows перед тестом и закрывает после.
    process = subprocess.Popen("calc.exe")
    time.sleep(2)  # Ждём открытия калькулятора
    yield
    # Закрываем калькулятор
    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)

@pytest.mark.order(1)
def test_addition(start_calculator):
    time.sleep(1)
    # Нажимаем 2 + 2 =
    pyautogui.press('2')
    pyautogui.press('add')  # Это '+'
    pyautogui.press('2')
    pyautogui.press('enter')  # Это '='
    time.sleep(1)
    # Копируем результат из калькулятора (Ctrl+C)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    result = pyperclip.paste()
    assert result.strip() == '4', f"Ожидали 4, но получили: {result}"
    time.sleep(3)


@pytest.mark.order(2)
def test_subtraction(start_calculator):
    time.sleep(1)
    pyautogui.press('8')
    pyautogui.press('subtract')  # Это '-'
    pyautogui.press('7')
    pyautogui.press('enter')  # Это '='
    time.sleep(1)
    # Копируем результат из калькулятора (Ctrl+C)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    result = pyperclip.paste()
    assert result.strip() == '1', f"Ожидали 1, но получили: {result}"
    time.sleep(3)


