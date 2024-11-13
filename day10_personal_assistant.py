# Если не рвботает код!!!
# 1. Пропиши "pip install pytz" в терминале
# 2. Пропиши "pip install requests" в терминале


# Импорт библиотек
import webbrowser
import subprocess
import pytz
from datetime import datetime
import requests

# Личный ассистент Kursk Assistant
while True:
    print("Вас приветствует Личный ассистент Kursk Assistant!")
    print()
    print("Программа написана группой Pied Piper, 2024 г.")
    print()
    print("1. Узнать погоду в Курске\n"
            "2. Перевести с английского на русский\n" 
            "3. Подсказать время\n"
            "4. Запустить приложение\n"
            "5. Разговоры\n"
            "6. Найти страницу в интернете\n"
            "7. Скачать Pudge Story Mode"
        )

    command = int(input("Напишите цифру задачи, которую Вы хотите задать Ассистенту."))
    if command == 1:
        print("Вы выбрали Узнать погоду в Курске\n!")
    # Функция, юзающая API openweathermap
        def get_weather(city):
            api_key = "e53f77fb758f64d423ba69ebf0f5167e"  # замените на ваш API-ключ
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            
            complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
            response = requests.get(complete_url)
            data = response.json()
            
            if "main" in data:
                main = data["main"]
                weather_desc = data["weather"][0]["description"]
                temperature = main["temp"]
                pressure = main["pressure"]
                humidity = main["humidity"]
                
                print(f"Погода в городе: Курск")
                print(f"Температура: {temperature}°C")
                print(f"Описание: {weather_desc}")
                print(f"Атмосферное давление: {pressure} hPa")
                print(f"Влажность: {humidity}%")
            else:
                if "cod" in data and data["cod"] != 200:
                    print(f"Ошибка: {data['message']} (код ошибки: {data['cod']})")
                else:
                    print("Не удалось получить данные о погоде.")

        get_weather("Kursk")
        print()
        print()
        break



    if command == 2:
        print("Вы выбрали Перевести с английского на русский!")
        # Да, всё настолько скучно, я устал(
        webbrowser.open("https://translate.google.ru/?sl=ru&tl=en&op=translate", new=2)
        break

    if command == 3:
        print("Вы выбрали Подсказать время!")
        print("Перед использованием возможно предстоит скачать библиотеку pytz, команда pip install pytz!\n")

        # Словарь с часовыми поясами для некоторых городов
        city_timezones = {
            "Курск": "Europe/Moscow",
            "Москва": "Europe/Moscow",
            "Нью-Йорк": "America/New_York",
            "Токио": "Asia/Tokyo",
            "Лондон": "Europe/London",
            "Париж": "Europe/Paris",
            "Сидней": "Australia/Sydney",
            "Кейптаун": "Africa/Johannesburg",
            "Дели": "Asia/Kolkata"
            }

        def get_current_time(city):
            if city in city_timezones:
                timezone = pytz.timezone(city_timezones[city])
                current_time = datetime.now(timezone)
                return current_time.strftime("%Y-%m-%d %H:%M:%S")
            else:
                return None

        # Ввод названия города
        city_name = input("Введите название города из предложенного списка (Курск, Москва, Нью-Йорк, Токио, Лондон, Париж, Сидней, Кейптаун, Дели): \n")

        # Получение текущего времени
        current_time = get_current_time(city_name)
        if current_time:
            print(f"Текущее время в {city_name}: {current_time}")
            break
        else:
            print("Город не найден в базе данных.\n")
            break


    if command == 4:
        print("Вы выбрали Запустить приложение!")

        def run_application(commande):
            try:
                # Запускаем команду
                process = subprocess.run(commande, check=True)
                print(f"Приложение завершилось с кодом: {process.returncode}")
            except subprocess.CalledProcessError as e:
                print(f"Произошла ошибка при запуске приложения: {e}")

        running = input("Введите название приложения (с расширением .exe)\n"
                        "К примеру notepad.exe для запуска Блокнота\n"
                        "Внимание! Доступны только программы в директории Path,\n"
                        "для запуска иных пропишите путь, пример: C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE\n")
        # Введите команду, которую хотите выполнить
        run_application([running])
        break
        # Пример: для запуска Notepad (Windows)
        # run_application(["notepad.exe"])
        # Запускаем приложение

    if command == 5:
        print("Вы выбрали Разговоры!")
        def chat_assistant():
            print("Привет! Я ваш асистент. Как я могу помочь вам сегодня?")
            print("Доступные команды:\n"
            "как дела\n"
            "погода\n"
            "что ты умеешь\n"
            "пока\n")
            while True:
                user_input = input("Вы: ")
                
                if user_input.lower() in ['exit', 'выход', 'пока']:
                    print("Ассистент: До свидания!")
                    break
                elif 'как дела' in user_input.lower():
                    print("Ассистент: У меня всё хорошо, спасибо!")
                elif 'погода' in user_input.lower():
                    print("Ассистент: Погода сегодня прекрасная!")
                elif 'что ты умеешь' in user_input.lower():
                    print("Ассистент: Я могу отвечать на вопросы и вести разговор!")
                else:
                    print("Ассистент: Простите, я не совсем понимаю вас.")

        chat_assistant()

    if command == 6:
        print("Вы выбрали Найти страницу в интернете!")
        search1 = input("Введите поисковый запрос.\n")
        # Проверяем наличие "https://" в вводе пользователя
        if "https://" in search1:
            webbrowser.open(search1, new=2)
            break
        else:
            search2 = "https://www.google.ru/search?q=" + search1
            webbrowser.open(search2, new=2)
            break
        # Мы просто складываем начальную сслыку поиска гугл "https://www.google.ru/search?q=" и ваш запрос (search1)
        # и получаем рабочий поисковик (если вставлять ссылки, то работает настройка if)

    if command == 7:
        print("Вы выбрали Скачать Pudge Story Mode!")
        webbrowser.open("https://t.me/kurskgamestudios", new=2)
    break