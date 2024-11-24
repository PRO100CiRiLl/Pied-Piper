# Конвертер температур

# Функция перевода в Цельсий в Фаренгейт
def cel_to_fahr(celsius):
    return (celsius * 9/5) + 32

# Функция перевода в Фаренгейт в Цельсий
def fahr_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Добро пожаловать в Конвертер температур!")
print("1. Цельсий в Фаренгейт")
print("2. Фаренгейт в Цельсий")

# Опрдеелние выбора пользователя
choice = input("Выберите конверсию (1 или 2): ")

if choice == '1':
    celsius = float(input("Введите температуру в Цельсии: "))
    print(f"{celsius}°C = {cel_to_fahr(celsius)}°F")

elif choice == '2':
    fahrenheit = float(input("Введите температуру в Фаренгейте: "))
    print(f"{fahrenheit}°F = {fahr_to_cel(fahrenheit)}°C")

else:
    print("Неверный ввод!")