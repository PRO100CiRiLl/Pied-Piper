# Kursk OS

class KurskOS:
    def __init__(self):
        self.running = True
        self.files = {}  # Словарь для хранения файлов

    def run(self):
        print("--------------------------\n"
            "Добро пожаловать в Kursk OS\n"
            "         1()1\n"
            "       2  ()  2\n"
            "     3    ()    3\n"
            "--------------------------\n"
            "2024y All right reserved\n")

        print("Введите команду (echo, ls, touch, cat, add, helpy, exit):")

        while self.running:
            command = input("> ").strip()
            self.execute_command(command)

    def execute_command(self, command):
        if command.startswith("echo "):
            text_to_echo = command[5:]
            self.echo(text_to_echo)
        elif command == "helpy":
            self.helpy()
        elif command == "ls":
            self.ls()
        elif command.startswith("touch "):
            filename = command[6:]
            self.touch(filename)
        elif command.startswith("cat "):
            filename = command[4:]
            self.cat(filename)
        elif command.startswith("add "):
            self.add_text_to_file(command)
        elif command == "exit":
            self.exit_os()
        else:
            print(f"Неизвестная команда: {command}")

    def helpy(self):
        print("Описание команд:\n"
            "1. echo [текст]: Выводит текст на экран.\n"
            "2. ls: Показывает список существующих файлов в системе.\n"
            "3. touch [имя файла]: Создаёт новый файл с указанным именем.\n"
            "4. cat [имя файла]: Выводит содержимое указанного файла (пока что все файлы пусты).\n"
            "5. add [имя файла] {ваш текст} - добавляет текст в файл.\n"
            "6. exit: Завершает выполнение операционной системы.\n"
            "--------------------------\n")

    def echo(self, text):
        print(text)

    def ls(self):
        print("Список файлов:")
        if self.files:
            for filename in self.files.keys():
                print(filename)
        else:
            print("(пусто)")

    def touch(self, filename):
        if filename in self.files:
            print(f"Файл '{filename}' уже существует.")
        else:
            self.files[filename] = ""  # Создаем пустой файл
            print(f"Создан файл '{filename}'.")

    def cat(self, filename):
        if filename in self.files:
            print(f"Содержимое файла '{filename}':")
            print(self.files[filename] if self.files[filename] else "(пусто)")
        else:
            print(f"Файл '{filename}' не найден.")

    def add_text_to_file(self, command):
        parts = command.split(" ", 2)  # Делим команду на части
        if len(parts) < 3:
            print("Использование: add [имя файла] [текст]")
            return

        filename = parts[1]
        text_to_add = parts[2]  # Возвращаем все, что после имени файла

        if filename not in self.files:
            self.files[filename] = text_to_add  # Создать файл и добавить текст
            print(f"Файл '{filename}' был создан и текст добавлен.")
        else:
            self.files[filename] += "\n" + text_to_add  # Добавить текст к существующему файлу
            print(f"Текст был добавлен в файл '{filename}'.")


    def exit_os(self):
        print("--------------------------\n"
            "         1(0)1\n"
            "       2  (0)  2\n"
            "     3    (0)    3\n"
            "--------------------------\n"
        
            "Завершение работы операционной системы...")
        self.running = False

# Запуск операционной системы
if __name__ == "__main__":
    os_instance = KurskOS()
    os_instance.run()