import time
from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList

def test_insertion(n=10000):
    # Stack
    start = time.time()
    stack = Stack()
    for i in range(n):
        stack.push(i)
    stack_time = time.time() - start
    
    # Queue
    start = time.time()
    queue = Queue()
    for i in range(n):
        queue.enqueue(i)
    queue_time = time.time() - start
    
    # Linked List (append)
    start = time.time()
    lst = SinglyLinkedList()
    for i in range(n):
        lst.append(i)
    list_time = time.time() - start
    
    return stack_time, queue_time, list_time