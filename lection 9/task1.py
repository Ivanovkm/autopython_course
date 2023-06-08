# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt
from pathlib import Path


class FileChanger:
    """
    Класс для работы с файлами. Принимает на вход имя входного файла, имя для выходного.
    """
    def __init__(self, in_f, out_f):
        self.in_path = Path(Path.cwd(), 'test_file', in_f)
        self.out_path = Path(Path.cwd(), 'test_file', out_f)
        self.file_string = ''

    def del_nums(self):
        """
        Функция удаляет из текста файла все цифры и на выходе создает новый файл с текстом без цифр
        """
        try:
            with open(self.in_path, 'r', encoding='UTF-8') as file:
                self.file_string = file.read()
        except FileNotFoundError as e:
            print(e, 'Не удалось открыть файл')

        for i in range(10):
            if str(i) in self.file_string:
                self.file_string = self.file_string.replace(str(i), '')
        try:
            with open(self.out_path, 'w', encoding='UTF-8') as out:
                out.write(self.file_string)
        except OSError as e:
            print(e, "Ошибка при записи в файл")


FileChanger('task1_data.txt', 'task1_answer.txt').del_nums()

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
