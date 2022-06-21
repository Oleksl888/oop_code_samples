"""
Взяв за основу код примера 06-iterable_with_an_iterator.py, расширьте функциональность класса MyList,
добавив методы для очистки списка, добавления элемента в произвольное место списка, удаления
элемента из конца и произвольного места списка.
"""


class MyList(object):
    class _ListNode(object):
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        # Длина списка
        self._length = 0
        # Первый элемент списка
        self._head = None
        # Последний элемент списка
        self._tail = None

        # Добавление всех переданных элементов
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def pop(self): # delete last element in the list
        self._tail = self._tail.prev
        self._tail.next = None
        self._length -= 1

    def remove(self, index):
        if index > self._length - 1:
            raise IndexError
        elif index == self._length -1:
            self.pop()
        else:
            if index != 0:
                current = self._head
                for _ in range(index):
                    current = current.next
                previous = current.prev
                next = current.next
                previous.next = current.next
                next.prev = current.prev
                del current
            else:
                x = self._head.next
                self._head = x
                self._head.prev = None
            self._length -=1

    def clean(self):
        self._head = None
        self._tail = None
        self._length = 0

    def insert(self, position, element):
        if position > self._length:
            raise IndexError
        elif position == self._length:
            self.append(element)
        else:
            node = MyList._ListNode(element)
            current = self._head
            if position != 0:
                for _ in range(position):
                    current = current.next
                node.next = current
                previous = current.prev
                previous.next = node
                node.prev = previous
            elif position == 0:
                node.next = self._head
                self._head.prev = node
                self._head = node
            self._length += 1

    def append(self, element):
        """Добавление элемента в конец списка"""

        # Создание элемента списка
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def __len__(self):
        return self._length

    def __repr__(self):
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        current = self._head
        for _ in range(self._length):
            yield current.value
            current = current.next


def main():
    # Создание списка
    my_list = MyList([1, 2, 5, 10, 20])

    # Вывод длины списка
    print(len(my_list))

    # Вывод самого списка
    print(my_list)

    print()

    # Обход списка
    for element in my_list:
        print(element)

    print()

    my_list.insert(0, 100)
    my_list.remove(1)
    my_list.remove(0)
    # Повторный обход списка
    for element in my_list:
        print(element)


if __name__ == '__main__':
    main()