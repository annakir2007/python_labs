from typing import Any, Optional, Iterator


class Node:
    '''Узел односвязного списка'''
    
    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.next: Optional['Node'] = None
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


class SinglyLinkedList:
    '''Односвязный список'''
    
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0
    
    def append(self, value: Any) -> None:
        '''Добавить элемент в конец списка. O(1) с tail, O(n) без tail'''
        new_node = Node(value)
        
        if self.head is None:  # Список пустой
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: Any) -> None:
        '''Добавить элемент в начало списка. O(1)'''
        new_node = Node(value)
        
        if self.head is None:  # Список пустой
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self._size += 1
    
    def insert(self, idx: int, value: Any) -> None:
        '''
        Вставить элемент по индексу.
        O(1) если вставка в начало, O(n) если в середину/конец
        '''
        if idx < 0 or idx > self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size}]")
        
        if idx == 0:  # Вставка в начало
            self.prepend(value)
            return
        
        if idx == self._size:  # Вставка в конец
            self.append(value)
            return
        
        # Вставка в середину
        new_node = Node(value)
        current = self.head
        for _ in range(idx - 1):  # Дойти до элемента перед idx
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self._size += 1
    
    def remove_at(self, idx: int) -> None:
        '''
        Удалить элемент по индексу.
        O(1) если удаление из начала, O(n) если из середины/конца
        '''
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size - 1}]")
        
        # Удаление первого элемента
        if idx == 0:
            self.head = self.head.next
            if self.head is None:  # Если список стал пустым
                self.tail = None
            self._size -= 1
            return
        
        # Удаление из середины или конца
        current = self.head
        for _ in range(idx - 1):  # Дойти до элемента перед idx
            current = current.next
        
        # Удаляем элемент current.next
        if current.next == self.tail:  # Удаляем последний элемент
            self.tail = current
        
        current.next = current.next.next
        self._size -= 1
    
    def remove(self, value: Any) -> bool:
        '''
        Удалить первое вхождение значения.
        Возвращает True если элемент удалён, False если не найден.
        O(n)
        '''
        if self.head is None:
            return False
        
        # Удаление первого элемента
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return True
        
        # Поиск в остальной части списка
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        
        if current.next is None:  # Элемент не найден
            return False
        
        # Найден элемент для удаления
        if current.next == self.tail:  # Удаляем последний элемент
            self.tail = current
        
        current.next = current.next.next
        self._size -= 1
        return True
    
    def __iter__(self) -> Iterator[Any]:
        '''Итератор по значениям списка'''
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self) -> int:
        '''Количество элементов в списке. O(1)'''
        return self._size
    
    def __repr__(self) -> str:
        # Первый вариант: простой
        # values = list(self)
        # return f"SinglyLinkedList({values})"
        
        # Второй вариант: "красивый" вывод
        if self.head is None:
            return "SinglyLinkedList: None"
        
        parts = []
        current = self.head
        while current is not None:
            parts.append(f"[{current.value}]")
            current = current.next
        
        return "SinglyLinkedList: " + " -> ".join(parts) + " -> None"
    
    def __str__(self) -> str:
        '''Графическое представление списка'''
        if self.head is None:
            return "None"
        
        result = []
        current = self.head
        while current is not None:
            result.append(f"[{current.value}]")
            current = current.next
        
        return " -> ".join(result) + " -> None"
    
if __name__ == "__main__":
    lst = SinglyLinkedList()
    
    lst.append(1)
    lst.append(2)
    lst.append(3)
    print(f"Добавили элементы в пустой список: {list(lst)}")
    
    lst.prepend(0)
    print(f"Добавили ноль в начало списка: {list(lst)}")

    lst.insert(2, 10)
    print(f"Вставили новый элемент на позицию 2: {list(lst)}")
    
    lst.remove(2)
    print(f"Убрали 2: {list(lst)}")
    
    print("Длина:", len(lst))
