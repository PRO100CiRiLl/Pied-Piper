
#Определяем функцию, для повторения цикла после расчёта ответа

def start():
    chifra1 = int(input("Вас приветствует калькулятор Kursk 3000v\n"
                        "-.-.-.-.-.-.-.-.-.-.-.-.-\n"
                        "Введите ваше число: "))
    chifra2 = int(input("Введите второе число "))
    print("Выберите математическую операцию:\n+\n-\n*\n/\n%")
    operation = input("Ваш выбор: ")

    while True:
        if operation == "+":
            print ("Сложение")
            result = chifra1 + chifra2
        elif operation == "-":
            print ("Вычитание")
            result = chifra1 - chifra2
        elif operation == "*":
            print ("Умножение")
            result = chifra1 * chifra2
        elif operation == "/":
            print ("Деление")
            if chifra2 != 0:
                    result = chifra1 / chifra2
                    print ("Результат:", result)
                    start() 
            else:
                print("Нельзя делить на ноль.")
                start() 
        elif operation == "%":
            print ("Деление без остатка")
            if chifra2 != 0:
                    result = chifra1 % chifra2
                    print ("Результат:", result)
                    start()
            else:
                print("Нельзя делить на ноль.")
                start() 
        else:
            print ("Ваша глупость привела к фатальной ошибке")
            print ("SyntaxError n404")

        #Результат
        print (chifra1, operation, chifra2, "Результат:", result)
        start()
#Здесь начинается и заканчивается код 
print (start())
