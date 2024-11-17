# Генератор паролей

# Импорт библиотек
import random

# Список символов для генерации паролей (2 списка)
chars_cyrillic = "+-/*!&$#?=@<>абвгдеёжзийклмнопрстуфхцчшщьъэюяabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
chars_latin = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Начало программы
print("Добро пожаловать в Генератор паролей!")
choice = input("Выберите режим генерации (напишите 1 или 2):\n"
                "1. С кириллицей и латинскими символами\n"
                "2. Только латиница\n")

# Проверка выбора пользователя
if choice == '1':
    chars = chars_cyrillic
elif choice == '2':
    chars = chars_latin
else:
    print("Ошибка, выберите 1 или 2.")
    exit(1)  # Завершить программу при ошибочном выборе

# Запрос количества паролей и длины пароля
number = input('Количество паролей? (введите число)\n')
length = input('Длина пароля? (введите число)\n')

# Преобразование входных данных в целые числа
try:
    number = int(number)
    length = int(length)
except ValueError:
    print("Ошибка: введите корректные числа для количества и длины пароля.")
    exit(1)

# Генерация и вывод паролей
for n in range(number):
    password = ''.join(random.choice(chars) for _ in range(length))
    print(password)