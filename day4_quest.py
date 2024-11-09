import tkinter as tk
from tkinter import messagebox

# Основной текст квеста
quest_text = {
    "main": [
        "Вы идёте по тёмному лесу. Вокруг гробовая тишина, неслышно даже шум ветра, который колышит листву.",
        "Вы шагаете по узкой тропинке, которая должна вывести Вас отсюда.",
        "Спустя некоторое время тропинка исчезает и вы понимаете что дальше придётся идти наугад.",
        "Вы проходите ещё немного и вдруг на вас выскакивает...",
        "...Яростный Пудж, он направляется вам навстречу со страшной гримасой.",
    ],
    "choice": "1. Стоять на месте.\n2. Попытаться сбежать\n3. #$@I@#!#.",
    "choice_1": [
        "Вы стоите на месте.",
        "Пудж подходит к вам.\nОн достаёт свой хук и с размаху бьёт по голове.",
        "Вы упали в обморок, больше никогда не придя в сознание.",
        "Концовка: ЛОШАРА."
    ],
    "choice_2": [
        "Вы бежите от страшного Пуджа,\nПытаясь спрятаться в кустах.",
        "Кажется вам это удаётся. Пудж исчез.",
        "Вы успокаиваетесь, однако вдруг в ваши кусты залазит...",
        "...Мишка Фредди, этот медведь начинает вопить и стараться поймать вас.",
        "Вы бьёте наглого медведя по морде, и выбегаете из кустов.",
        "Вдруг откуда ни возьмись возвращается Пудж, вы понимаете, что окружены.\nОднако, несмотря на плачевную ситуацию, вы слышите звук автомобиля...",
        "Похоже у вас появилась надежда.",
        "Это едет Сиреноголовый, он кричит вам немедленно садиться в автотранспортное средство.",
        "Вы немедленно садитесь в авто. Сиреноголовый газует, и Фредди с Пуджом остаются в дураках.",
        "Концовка: РЕСПЕКТ"
    ],
    "choice_3": ["Куда ты жмал."]
}

# Инициализация приложения
root = tk.Tk()
root.title("Интерактивный Квест")
root.geometry("500x400")

text_index = 0
current_choice = "main"

# Функция для отображения следующей строки текста
def next_text():
    global text_index, current_choice
    if current_choice == "main" and text_index == len(quest_text["main"]):
        display_text(quest_text["choice"])
        text_index = 0
    elif current_choice == "main":
        display_text(quest_text[current_choice][text_index])
        text_index += 1
    elif current_choice in ["choice_1", "choice_2", "choice_3"] and text_index < len(quest_text[current_choice]):
        display_text(quest_text[current_choice][text_index])
        text_index += 1
    else:
        restart_game()

# Функция для выбора действия
def make_choice(choice):
    global text_index, current_choice
    text_index = 0
    if choice == 1:
        current_choice = "choice_1"
    elif choice == 2:
        current_choice = "choice_2"
    elif choice == 3:
        current_choice = "choice_3"
    next_text()

# Функция для отображения текста в интерфейсе
def display_text(text):
    text_widget.config(state="normal")
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, text)
    text_widget.config(state="disabled")

# Функция для рестарта игры
def restart_game():
    global text_index, current_choice
    text_index = 0
    current_choice = "main"
    next_text()

# Виджет для отображения текста
text_widget = tk.Text(root, wrap="word", height=15, width=50, state="disabled", bg="black", fg="green")
text_widget.pack(pady=10)

# Кнопки управления
button_frame = tk.Frame(root)
button_frame.pack()

continue_button = tk.Button(button_frame, text="Продолжить", command=next_text)
continue_button.grid(row=0, column=0, padx=10)

choice1_button = tk.Button(button_frame, text="1", command=lambda: make_choice(1))
choice2_button = tk.Button(button_frame, text="2", command=lambda: make_choice(2))
choice3_button = tk.Button(button_frame, text="3", command=lambda: make_choice(3))

choice1_button.grid(row=0, column=1, padx=5)
choice2_button.grid(row=0, column=2, padx=5)
choice3_button.grid(row=0, column=3, padx=5)

restart_button = tk.Button(button_frame, text="Рестарт", command=restart_game)
restart_button.grid(row=0, column=4, padx=10)

# Запуск игры
next_text()
root.mainloop()