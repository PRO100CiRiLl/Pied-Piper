
#Импортируем библиотеку
import random
trying = 0
while True:
    #Запрашиваем имя пользователя (MSHK FREDE)
    name = input("Вас приветствует Угадыватель Чисел Kursk\n"
                "Как Вас зовут?\n")
    num = random.randint(1,25)
    if name == "MSHK FREDE":
        print ("АААААА МШК ФРЕДЕ!1!1!1!\n")
    else:
        print ("Привет,", name, "! Я загадал число от 1 до 25, попробуй угадай.")

    print (name, "Выбери режим игры:\n"
        "1 - Средняя сложность: 5 попыток\n"
        "2 - Высокая сложность: 3 попытки\n")
    #Ввод числа
    vibor = int(input())
    #Средняя сложность

    if vibor == 1:
        print ("Средняя сложность: 5 попыток (Числа от 1 до 25)\n")
        while trying < 5:
            guess = int(input("Введите число: "))
            trying +=1

            if guess < num:
                print ("Твоё число меньше загадонного.")
            if guess > num:
                print ("Твоё число больше загадонного.")
            if guess == num:
                break
        if guess == num:
            print(name, ", ты смог угадать число, использовав", format(trying),"попыток!")
        else:
            print("Не угадал, я загадал число ", format(num))
    #Высокая сложность
    elif vibor ==2:
        print ("Высокая сложность: 3 попытки (Числа от 1 до 25)\n")
        while trying < 3:
            guess = int(input("Введите число: "))
            trying +=1

            if guess < num:
                print ("Твоё число меньше загадогного.")
            if guess > num:
                print ("Твоё число больше загадогного.")
            if guess == num:
                break
        if guess == num:
            print(name, ", ты смог угадать число, использовав", format(trying),"попыток!")
        else:
            print("Не угадал, я загадал число ", format(num))
    # Ошибка с выбором сложности    
    else:
        print("Введи число 1 или 2!")