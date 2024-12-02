import os
import time

import pyautogui

os.system("gnome-calculator &")

# Ждем, чтобы калькулятор успел открыться
time.sleep(3)


# Функция для нажатия кнопки на калькуляторе
def press_button(button_image):
    try:
        button_location = pyautogui.locateOnScreen(button_image, confidence=0.9)
        if button_location:
            pyautogui.click(button_image)
    except pyautogui.ImageNotFoundException:
        print(f"Кнопка {button_image} не найдена на экране.")


# Нажимаем кнопки для 12 + 7
press_button("1.png")  # Изображение кнопки '1'
press_button("2.png")  # Изображение кнопки '2'
press_button("plus.png")  # Изображение кнопки '+'
press_button("7.png")  # Изображение кнопки '7'
press_button("equals.png")  # Изображение кнопки '='
