# Эта часть кода показывает пример работы кода
print("Данный код считает количетсво слов в строке.")
s = "Это наш пример строки"
print(s)
words = s.split()
#Измерение количества слов
num_words = len(words)
print("Слов в строке:", num_words)
#Начало цикла счёта количества слов в строках
while True:
    word_user = input("Введите вашу строку, чтобу посчитать количество строк.")
    words_user = word_user.split()
    num_words_user = len(words_user)
    print("Слов в строке:", num_words_user)
    break

