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

