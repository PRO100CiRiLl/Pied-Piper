# Создание и визуализация таблиц

#Функция списка
def format_list_with_borders(lst):
    # Форматирование списка с перегородками сверху и снизу
    if not lst:  # Если список пустой
        return "-----\nСписок пуст.\n-----"
    
    header_footer = "-----"  # Перегородка
    formatted_list = "\n".join(map(str, lst))  # Объединяем элементы списка в строку
    return f"{header_footer}\n{formatted_list}\n{header_footer}"  # Полное форматирование 

def edit_list(lst):
    # Основной цикл программы
    while True:
        print("Вас приветствует Создатель Таблиц KURSK228!!!!")
        print(format_list_with_borders(lst))
        print("1. Добавить элемент")
        print("2. Удалить элемент")
        print("3. Выйти\n")
        
        choice = input("Выберите действие: ")
        
        # Добавление элемента в список
        if choice == "1":
            element = input("Введите элемент для добавления: ")
            lst.append(element)
            print(f"Элемент '{element}' добавлен в список.")
        # Удаление элемента из списка
        elif choice == "2":
            element = input("Введите элемент для удаления: ")
            if element in lst:
                lst.remove(element)
                print(f"Элемент '{element}' удален из списка.")
            else:
                print("Такого элемента нет в списке.")
        # Завершение работы
        elif choice == "3":
            print("Выход из программы...")
            print("Итоговый список:\n", format_list_with_borders(lst))
            break
        else:
            print("Неверно. Пожалуйста, выберите одно из предложенных действий.")

# Инициализируем список
my_list = [1, 2, "kagms", "Pudge SM"]
edit_list(my_list)  # Запускаем функцию редактирования списка

# Итоговый список будет отображаться сразу в процессе редактирования