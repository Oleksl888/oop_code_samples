'''Создайте класс Editor, который содержит методы view_document и edit_document. Пусть метод
edit_document выводит на экран информацию о том, что редактирование документов недоступно для
бесплатной версии. Создайте подкласс ProEditor, в котором данный метод будет переопределён.
Введите с клавиатуры лицензионный ключ и, если он корректный, создайте экземпляр класса ProEditor,
иначе Editor. Вызовите методы просмотра и редактирования документов.'''


class Editor:
    def __init__(self, document):
        self.document = document

    def view_document(self):
        print(f'Opening for reading filename: {self.document}')
        print('-------------------------------------------')

    @staticmethod
    def edit_document():
        print('Editing unavaliable for the free version')


class ProEditor(Editor):
    def edit_document(self):
        print(f'Opening for editing filename: {self.document}')
        print('-------------------------------------------')


if __name__ == '__main__':
    key = '12345'
    password = input('Please enter licence key: ')
    if password == key:
        editor = ProEditor('Document.xls')
    else:
        editor = Editor('Document.xls')

    editor.view_document()
    editor.edit_document()
