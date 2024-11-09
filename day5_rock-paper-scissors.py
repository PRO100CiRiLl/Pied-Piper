#Импортируем библиотеку
import random
print("Добро пожаловать в игру Камень-ножницы-бумага!")
while True:
    user_choice = input ("Камень, ножницы или бумага?")
    
    #Рандомайзер
    computer_list_choice = ["камень", "ножницы", "бумага"]
    computer_action = random.choice (computer_list_choice)
    print(f"\nВы выбрали {user_choice}, ваш противник - {computer_action}.\n")
    #Условия игры
    if user_choice == computer_list_choice:
        print(f"Оба игрока выбрали {user_choice}, ничья!")
    elif user_choice == "камень":
        if computer_action == "ножницы":
            print("Камень бьет ножницы! Вы победили!")
        else:
            print("Бумага оборачивает камень! Вы проиграли.")
    elif user_choice == "бумага":
        if computer_action == "камень":
            print("Бумага оборачивает камень! Вы победили!")
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
    elif user_choice == "ножницы":
        if computer_action == "бумага":
            print("Ножницы режут бумагу! Вы победили!")
        else:
            print("Камень бьет ножницы! Вы проиграли.")
#Создание цикла
    again = "" 
    again = input("Сыграем еще? (д/н): ") 
    if again.lower() != "д": 
        break 
    else:
        print("Ок")