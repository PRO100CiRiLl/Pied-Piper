# Крестики - нки

# Основная программа
# Инициализация карты
map = [1,2,3,
        4,5,6,
        7,8,9]
 
# Инициализация победных линий
victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
 
# Вывод карты на экран
def draw_maps():
    print(map[0], end = " ")
    print(map[1], end = " ")
    print(map[2])
 
    print(map[3], end = " ")
    print(map[4], end = " ")
    print(map[5])
 
    print(map[6], end = " ")
    print(map[7], end = " ")
    print(map[8]) 

# Сделать ход в ячейку
def step_maps(step,symbol):
    ind = map.index(step)
    map[ind] = symbol

# Получить текущий результат игры
def get_result():
    win = ""
    
    for i in victories:
        if map[i[0]] == "X" and map[i[1]] == "X" and map[i[2]] == "X":
            win = "X"
        if map[i[0]] == "H" and map[i[1]] == "H" and map[i[2]] == "H":
            win = "H"   
                
    return win


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Функция для игры с человеком
def starthumans():
    game_over = False
    player1 = True
    
    while game_over == False:
    
        # 1. Показываем карту
        draw_maps()
    
        # 2. Спросим у играющего куда делать ход
        if player1 == True:
            symbol = "X"
            step = int(input("Человек 1, ваш ход: "))
        else:
            symbol = "H"
            step = int(input("Человек 2, ваш ход: "))
    
        step_maps(step,symbol) # делаем ход в указанную ячейку
        win = get_result() # определим победителя
        if win != "":
            game_over = True
        else:
            game_over = False
    
        player1 = not(player1)        
    
    # Игра окончена. Покажем карту. Объявим победителя.        
    draw_maps()
    print("Победил", win) 


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Часть кода для работы с ИИ
# Искусственный интеллект: поиск линии с нужным количеством X и O на победных линиях
def check_line(sum_H,sum_X):
 
    step = ""
    for line in victories:
        o = 0
        x = 0
 
        for j in range(0,3):
            if map[line[j]] == "H":
                o = o + 1
            if map[line[j]] == "X":
                x = x + 1
 
        if o == sum_H and x == sum_X:
            for j in range(0,3):
                if map[line[j]] != "H" and map[line[j]] != "X":
                    step = map[line[j]]
                 
    return step
 
# Искусственный интеллект: выбор хода
def AI():        
 
    step = ""
 
    # 1) если на какой либо из победных линий 2 свои фигуры и 0 чужих - ставим
    step = check_line(2,0)
 
    # 2) если на какой либо из победных линий 2 чужие фигуры и 0 своих - ставим
    if step == "":
        step = check_line(0,2)        
 
    # 3) если 1 фигура своя и 0 чужих - ставим
    if step == "":
        step = check_line(1,0)           
 
    # 4) центр пуст, то занимаем центр
    if step == "":
        if map[4] != "X" and map[4] != "H":
            step = 5           
 
    # 5) если центр занят, то занимаем первую ячейку
    if step == "":
        if map[0] != "X" and map[0] != "H":
            step = 1           
   
    return step
 
# Функция для игры с ИИ
def startai():
    game_over = False
    human = True
    
    while game_over == False:
    
        # 1. Показываем карту
        draw_maps()
    
        # 2. Спросим у играющего куда делать ход
        if human == True:
            symbol = "X"
            step = int(input("Человек, ваш ход: "))
        else:
            print("Компьютер делает ход: ")
            symbol = "H"
            step = AI()
    
        # 3. Если компьютер нашел куда сделать ход, то играем. Если нет, то ничья.
        if step != "":
            step_maps(step,symbol) # делаем ход в указанную ячейку
            win = get_result() # определим победителя
            if win != "":
                game_over = True
            else:
                game_over = False
        else:
            print("Ничья!")
            game_over = True
            win = "дружба"
    
        human = not(human)        
    
    # Игра окончена. Покажем карту. Объявим победителя.        
    draw_maps()
    print("Победил", win)   

print("Добро пожаловать в крестики - нки!")
select = int(input("Ввыберите режим игры:\n"
    "1. С человеком\n"
    "2. С искусственным интеллектом\n"
    "Напишите число 1 или 2\n"
))
if select == 1:
    print("Вы выбрали режим - С человеком")
    starthumans()
elif select == 2:
    print("Вы выбрали режим - С искусственным интеллектом")
    startai()
else:
    print("Ошибка инициализации.")