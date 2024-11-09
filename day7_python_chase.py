# Импорт библиотек
from tkinter import *
from random import randint

print("Добро пожаловать в игру Побег Питона от Kursk Game Studios!")
print("Выберите стиль игры:")
print("1 - Питон edition (жёлтая змея, красная еда)")
print("2 - Классический (зелёная змея, красная еда)")
print("3 - Тёмный (серая змея, белая еда)")

# Получаем выбор от пользователя
style_choice = input("Введите номер стиля: ")

# Устанавливаем цвета змеи и еды в зависимости от выбора пользователя
if style_choice == "1":
    snake_color = "yellow"
    food_color = "red"
elif style_choice == "2":
    snake_color = "green"
    food_color = "red"
elif style_choice == "3":
    snake_color = "gray"
    food_color = "white"
else:
    print("Неверный ввод. Запуск в стандартном стиле.")
    snake_color = "yellow"
    food_color = "red"


class Game:
    # Основа игры
    def __init__(self, canvas):
        self.canvas = canvas
        self.snake_coords = [[14, 14]]
        self.eat_coords = [randint(0, 29) for _ in range(2)]
        self.vector = {"Up": (0, -1), "Down": (0, 1), "Left": (-1, 0), "Right": (1, 0)}
        self.direction = self.vector["Right"]
        self.canvas.focus_set()
        self.canvas.bind("<KeyPress>", self.set_direction)
        self.GAME()

    # Изменение положения еды
    def set_eat(self):
        self.eat_coords = [randint(0, 29) for _ in range(2)]
        # Чтоб еда не спавнилась на змее
        if self.eat_coords in self.snake_coords:
            self.set_eat()

    # Изменение направления змеи (вроде)
    def set_direction(self, event):
        # Если (if) кнопка нажата
        if event.keysym in self.vector:
            self.direction = self.vector[event.keysym]

    # Отрисовка игры
    def draw(self):
        self.canvas.delete(ALL)
        x_eat, y_eat = self.eat_coords
        self.canvas.create_rectangle(x_eat * 10, y_eat * 10, (x_eat + 1) * 10, (y_eat + 1) * 10, fill=food_color, width=0)
        for x, y in self.snake_coords:
            self.canvas.create_rectangle(x * 10, y * 10, (x + 1) * 10, (y + 1) * 10, fill=snake_color, width=0)

    # Содание координат от 0 до 29 [0, 29]
    @staticmethod
    def coord_check(coord):
        return 0 if coord > 29 else 29 if coord < 0 else coord

    # Алгоритм "Оторванный Хвост\Логика игры"  
    def GAME(self):
        self.draw()
        x, y = self.snake_coords[0]
        x += self.direction[0]
        y += self.direction[1]
        x = self.coord_check(x)
        y = self.coord_check(y)
        if x == self.eat_coords[0] and y == self.eat_coords[1]:
            self.set_eat()
        elif [x, y] in self.snake_coords:
            self.snake_coords = []
        else:
            self.snake_coords.pop()
        self.snake_coords.insert(0, [x, y])
        self.canvas.after(100, self.GAME)


# Не знаю что это делает (хотя кому какая разница)
root = Tk()
canvas = Canvas(root, width=300, height=300, bg="black")
canvas.pack()
game = Game(canvas)
root.mainloop()