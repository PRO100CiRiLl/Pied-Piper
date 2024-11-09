#Испортируем библиотеку
import random
 
#Понятия не имею что это значит, я украл код
x = "д"

print("Добро пожаловать в генератор числа от 0 до 9 в формате Кости KURSK ROLL Generator v2!")  
while x == "д":
    # Генерируем 10 рандомных чисел
    # От 0 до 9 соответственно
    kubik = random.randint(0,9)
     
    if kubik == 0:
        print("[     ]")
        print("[     ]")
        print("[     ]")
    if kubik == 1:
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
    if kubik == 2:
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
    if kubik == 3:
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
    if kubik == 4:
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
    if kubik == 5:
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
    if kubik == 6:
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
    if kubik == 7:
        print("[0 0 0]")
        print("[  0  ]")
        print("[0 0 0]")
    if kubik == 8:
        print("[0 0 0]")
        print("[0   0]")
        print("[0 0 0]")
    if kubik == 9:
        print("[0 0 0]")
        print("[0 0 0]")
        print("[0 0 0]")
         
    x=input("Введите д, чтобы кинуть кость опять и н, чтобы выйти:")
    print("\n")