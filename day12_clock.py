# Часы, обратный отсчёт и секундомер
#Импорт библиотеки
import os
import time
import threading
from datetime import datetime

# Функция обратного отсчета
def countdown(seconds):
    print(f"Обратный отсчет начался: {seconds} секунд")
    for i in range(seconds, 0, -1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Обратный отсчет: {i} секунд")
        time.sleep(1)
    print("Обратный отсчет завершен!")

# Функция секундомера
def stopwatch():
    print("Секундомер запущен! Нажмите 'Enter' для остановки.")
    start_time = time.time()
    try:
        while True:
            elapsed_time = time.time() - start_time
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Секундомер: {elapsed_time:.2f} секунд")
            time.sleep(0.1)  # цикл каждые 0.1 секунды
    except KeyboardInterrupt:
        # Для корректного завершения при нажатии Ctrl+C
        pass

def clear_terminal():
    # Очистка терминала для разных операционных систем
    os.system('cls' if os.name == 'nt' else 'clear')

def display_time_and_options():
    while True:
        clear_terminal()
        # Получаем текущее время
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")

        # Выводим текущее время
        print("Добро пожаловть в Часы, обратный отсчёт и секундомер!")
        print("Текущее время:", current_time)
        print("1. Обратный отсчет")
        print("2. Секундомер")
        print("Введите 'выход' для выхода")

        # Обработка ввода пользователя
        user_input = input("Введите номер операции: ")

        # Реакция на ввод
        if user_input == '1':
            seconds = int(input("Введите количество секунд для обратного отсчета: "))
            threading.Thread(target=countdown, args=(seconds,)).start()
        elif user_input == '2':
            threading.Thread(target=stopwatch).start()  # Запуск секундомера в новом потоке
        elif user_input.lower() == 'выход':
            break

# Запускаем основную функцию
display_time_and_options()