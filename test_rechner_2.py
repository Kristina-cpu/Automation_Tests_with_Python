import pyautogui
import pytest
import os
import time
from test_rechner import start_calculator
import pyperclip

@pytest.mark.order(3)
def test_mult_with_image(start_calculator):
    time.sleep(1)
    pyautogui.press('2')
    pyautogui.press('multiply')
    pyautogui.press('2')
    pyautogui.press('enter')
    time.sleep(1)
    # Путь к шаблону результата
    template_path = os.path.join('Result_4.png')
    time.sleep(2)

    location = pyautogui.locateOnScreen(template_path, confidence=0.9)  # работает только при наличии OpenCV
    assert location is not None, "Не удалось найти изображение результата '4' на экране"

@pytest.mark.order(4)
def test_divide_with_image(start_calculator):
    time.sleep(2)
    pyautogui.press('1')
    pyautogui.press('5')
    pyautogui.press('divide')
    pyautogui.press('5')
    pyautogui.press('enter')
    time.sleep(1)
    # Путь к шаблону результата
    template_path = os.path.join('Result_3.png')
    time.sleep(2)
    location = pyautogui.locateOnScreen(template_path, confidence=0.9)  # работает только при наличии OpenCV
    assert location is not None, "Не удалось найти изображение результата '4' на экране"

@pytest.mark.order(5)
def test_divide_by_zero(start_calculator):
    time.sleep(1)
    # 7 ÷ 0 =
    pyautogui.press('7')
    pyautogui.press('divide')
    pyautogui.press('0')
    pyautogui.press('enter')
    time.sleep(1)
    # Копируем результат
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    result = pyperclip.paste().strip().lower()
    # Проверяем, что калькулятор сообщает об ошибке
    assert (
        "divide by zero" in result
        or "нельзя делить на ноль" in result
        or "на ноль делить" in result
        or "cannot divide" in result
        or "teilen durch 0 nicht möglich"
    ), f"Ожидали сообщение об ошибке деления на ноль, но получили: {result}"
