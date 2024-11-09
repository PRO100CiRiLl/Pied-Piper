#Функция списка
def edit_list(lst):
    while True:
        print("Вас приветствует Создатель Таблиц KURSK228!!!!")
        print("Текущий список:", lst)
        print("1. Добавить элемент")
        print("2. Удалить элемент")
        print("3. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            element = input("Введите элемент для добавления: ")
            lst.append(element)
        elif choice == "2":
            element = input("Введите элемент для удаления: ")
            if element in lst:
                lst.remove(element)
            else:
                print("Такого элемента нет в списке.")
        elif choice == "3":
            break
        else:
            print("Неверно. Извиняйся.")
    
    return lst

my_list = [1, 2, "kagms", "Pudge SM"]
my_list = edit_list(my_list)
print("Итоговый список:", my_list)
print("Благодарим за использование Создателя Таблиц KURSK228!!")