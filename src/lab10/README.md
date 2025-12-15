# <h1>ЛР9<h1>

# <h4>group.py<h4>

## Структуры данных: Stack, Queue, Linked List и бенчмарки

### Теоретическая часть

#### Стек (Stack)
**Стек** — структура данных, работающая по принципу LIFO (Last In, First Out — последним пришёл, первым вышел).

**Основные операции:**
- `push(item)` — добавить элемент на вершину стека (O(1))
- `pop()` — удалить и вернуть верхний элемент (O(1))
- `peek()` — посмотреть верхний элемент без удаления (O(1))
- `is_empty()` — проверить, пуст ли стек (O(1))

#### Очередь (Queue)
**Очередь** — структура данных, работающая по принципу FIFO (First In, First Out — первым пришёл, первым вышел).

**Основные операции:**
- `enqueue(item)` — добавить элемент в конец очереди (O(1))
- `dequeue()` — удалить и вернуть первый элемент (O(1))
- `peek()` — посмотреть первый элемент без удаления (O(1))
- `is_empty()` — проверить, пуста ли очередь (O(1))

#### Связный список (Linked List)
**Односвязный список** — динамическая структура данных, состоящая из узлов, каждый из которых содержит значение и ссылку на следующий узел.

**Основные операции:**
- `append(value)` — добавить в конец (O(1) с tail, O(n) без)
- `prepend(value)` — добавить в начало (O(1))
- `insert(idx, value)` — вставить по индексу (O(n) в худшем случае)
- `remove(value)` — удалить значение (O(n))
- `remove_at(idx)` — удалить по индексу (O(n) в худшем случае)

### Реализация

#### Задание A
Вот код к этому заданию:

#### Классы Stack, Queue

```
from collections import deque
from typing import Any, Optional

class Stack:
    """Стек (LIFO) на базе list"""
    
    def __init__(self) -> None:
        self._data: list[Any] = []
    
    def push(self, item: Any) -> None:
        """Добавить элемент на вершину стека. O(1)"""
        self._data.append(item)
    
    def pop(self) -> Any:
        """Снять верхний элемент стека и вернуть его. O(1)"""
        if self.is_empty():
            raise IndexError("Нельзя извлечь из пустого стека")
        return self._data.pop()
    
    def peek(self) -> Optional[Any]:
        """Вернуть верхний элемент без удаления. O(1)"""
        if self.is_empty():
            return None
        return self._data[-1]
    
    def is_empty(self) -> bool:
        """Проверить, пуст ли стек. O(1)"""
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """Количество элементов в стеке. O(1)"""
        return len(self._data)
    
    def __repr__(self) -> str:
        return f"Stack({self._data})"


class Queue:
    """Очередь (FIFO) на базе collections.deque"""
    
    def __init__(self) -> None:
        self._data: deque[Any] = deque()
    
    def enqueue(self, item: Any) -> None:
        """Добавить элемент в конец очереди. O(1)"""
        self._data.append(item)
    
    def dequeue(self) -> Any:
        """Взять элемент из начала очереди. O(1)"""
        if self.is_empty():
            raise IndexError("Нельзя извлечь из пустой очереди")
        return self._data.popleft()
    
    def peek(self) -> Optional[Any]:
        """Вернуть первый элемент без удаления. O(1)"""
        if self.is_empty():
            return None
        return self._data[0]
    
    def is_empty(self) -> bool:
        """Проверить, пуста ли очередь. O(1)"""
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """Количество элементов в очереди. O(1)"""
        return len(self._data)
    
    def __repr__(self) -> str:
        return f"Queue({list(self._data)})"
    
if __name__ == "__main__":
    print('-----Stack-----')

    stack = Stack()
    stack.push('A')
    stack.push('B')
    stack.push('C')
    
    print(f'Снятие верхнего элемента стека: {stack.pop()}')
    print(f'Проверка, пустой ли стек: {stack.is_empty()}')
    print(f'Число сверху: {stack.peek()}')
    stack.push('D')
    print(f'Значение сверху после добавления элемента в стек: {stack.peek()}')
    print(f'Длина стека: {len(stack)}')
    print(f'Стек: {stack._data}')
    
    print('-----Queue-----')
    q = Queue()
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    q.enqueue('D')
    
    print(f'Значение первого элемента: {q.peek()}')
    q.dequeue()
    print(f'Значение первого элемента после удаления элемента: {q.peek()}')
    q.enqueue('E')
    print(f'Значение первого элемента после добавления элемента: {q.peek()}')
    print(f'Проверка, пустая ли очередь: {q.is_empty()}')
    print(f'Количество элементов в очереди: {len(q)}')
    print(f'Очередь: {q._data}')
```


![](./images/lb10/img_structures.png)

#### Задание B
Вот код к этому заданию:

#### Класс SinglyLinkedList

```
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
```

![](./images/lb10/img_linked_list.png)