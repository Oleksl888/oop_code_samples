'''Создайте два класса Directory (папка) и File (файл).
Класс Directory должен иметь следующие поля:
- название (name типа str);
- родительская папка (root типа Directory);
- список файлов (files типа список, состоящий из экземпляров File)
- список подпапок (sub_directories типа список, состоящий из экземпляров Directory).
Класс Directory должен иметь следующие поля:
- добавление папки в список подпапок (add_sub_directory принимающий экземпляр Directory и присваивающий поле root для принимаемого экземпляра);
- удаление папки из списка подпапок (remove_sub_directory, принимающий экземпляр Directory и обнуляющий у него поле root. Метод также удаляет папку из списка sub_directories).
- добавление файла в папку (add_file, принимающий экземпляр File и присваивающий ему поле directory - см. класс File ниже);
- удаление файла из папки (remove_file, принимающий экземпляр File и обнуляющий у него поле directory. Метод удаляет файл из списка files).
Класс File должен иметь следующие поля:
- название (name типа str);
- папка (directory типа Directory);'''


from typing import TypeVar, List


class Directory:
    def __init__(self):
        self.name: str = ''
        self.root: DirType = None
        self.files: List[File] = []
        self.sub_directories: List[Directory] = []

    def add_sub_directory(self, dir_obj: 'Directory'):
        dir_obj.root = self
        self.sub_directories.append(dir_obj)

    def remove_sub_directory(self, dir_obj: 'Directory'):
        dir_obj.root = None
        self.sub_directories.remove(dir_obj)

    def add_file(self, file_obj: 'File'):
        file_obj.directory = self
        self.files.append(file_obj)

    def remove_file(self, file_obj: 'File'):
        file_obj.directory = None
        self.files.remove(file_obj)


class File:
    def __init__(self):
        self.name: str = ""
        self.directory: DirType = None


DirType = TypeVar('DirType', Directory, None)

main_dir = Directory()
main_dir.name = 'main'

another_dir = Directory()
another_dir.name = 'another'

some_file = File()
some_file.name = 'file1'

main_dir.add_sub_directory(another_dir)
main_dir.add_file(some_file)

print(main_dir.name)
print(main_dir.files)
print(main_dir.root)
print(main_dir.sub_directories)
print('------------------------')
print(another_dir.name)
print(another_dir.files)
print(another_dir.root)
print(another_dir.sub_directories)
print('------------------------')
print(some_file.name)
print(some_file.directory)
