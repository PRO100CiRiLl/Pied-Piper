# Библиотека

# Импорт библиотеки
import json

# Функция для книги (сохранение названия, автора, года выпуска)
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} от {self.author} ({self.year})"

# Библиотека
library = ["1984 от Дж. Оруэлл (1948)"]

# Функция для добавления книги 
def add_book():
    title = input("Введите название книги: ").strip()
    author = input("Введите автора книги: ").strip()
    year = input("Введите год выпуска книги: ").strip()
    
    if not year.isdigit():
        print("Год должен быть числом. Книга не добавлена.")
        return
    
    library.append(Book(title, author, int(year)))
    print(f"Книга '{title}' добавлена в библиотеку.")

# Функция для показа библиотеки
def show_books():
    if not library:
        print("В библиотеке нет книг.")
    else:
        print("Список книг в библиотеке:")
        for index, book in enumerate(library, start=1):
            print(f"{index}. {book}")

# Функция для показа библиотеки
def remove_book():
    show_books()
    if library:
        try:
            index = int(input("Введите номер книги для удаления: ")) - 1
            if 0 <= index < len(library):
                removed_book = library.pop(index)
                print(f"Книга '{removed_book.title}' удалена из библиотеки.")
            else:
                print("Некорректный номер книги.")
        except ValueError:
            print("Пожалуйста, введите число.")

# Функция для сохранения библиотеки
def save_library():
    with open('library.json', 'w', encoding='utf-8') as f:
        json.dump([vars(book) for book in library], f)
    print("Библиотека сохранена.")

# Функция для загрузки библиотеки
def load_library():
    global library
    try:
        with open('library.json', 'r', encoding='utf-8') as f:
            books_data = json.load(f)
            library = [Book(**book) for book in books_data]
        print("Библиотека загружена.")
    except FileNotFoundError:
        print("Файл библиотеки не найден.")
    except json.JSONDecodeError:
        print("Ошибка чтения файла библиотеки.")

# Цикл
while True:
    print("\n1. Добавить книгу")
    print("2. Показать книги")
    print("3. Удалить книгу")
    print("4. Сохранить библиотеку")
    print("5. Загрузить библиотеку")
    print("6. Выход")
    choice = input("Выберите действие: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        show_books()
    elif choice == '3':
        remove_book()
    elif choice == '4':
        save_library()
    elif choice == '5':
        load_library()
    elif choice == '6':
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")