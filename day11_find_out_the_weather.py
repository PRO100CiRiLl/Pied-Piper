# Если не рвботает код!!!
# Пропиши "pip install requests" в терминале
#Импорт библиотеки
import requests



print("Добро пожаловать в Предсказатель Погоды 3001!\n")

# Определяем название города
pogoda = input("Напишите название города на английском\n"
               "К примеру Kursk или Moscow!\n")


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
                
            print(f"Погода в городе: {city}")
            print(f"Температура: {temperature}°C")
            print(f"Описание: {weather_desc}")
            print(f"Атмосферное давление: {pressure} hPa")
            print(f"Влажность: {humidity}%")
        else:
            if "cod" in data and data["cod"] != 200:
                print(f"Ошибка: {data['message']} (код ошибки: {data['cod']})")
            else:
                print("Не удалось получить данные о погоде.")

get_weather(pogoda)
print()
print()