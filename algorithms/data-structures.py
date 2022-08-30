""" Stacks

UseCases:
    - backtracking:
        + finding the correct path through a maze
    - compile-time memory management
        + programs use thme to store local data and procedure info
        + nested and recursive functions
     - depth-first search
     - undo(pop) / repo(push)
"""

class Stack:
    def __init__(self):
        self._data = []

    def push(self, node): # O(1)
        self._data.append(node)

    def pop(self): # O(1)
        return self._data.pop()

    def is_empty(self):
        return self._data == []

    def peek(self):
        if self.is_empty():
            return None
        return self._data[-1]

    def get_stack(self):
        return self._data

""" Queues

UseCases:
    - breadth-first search

Collections.deque = doubly linked list
"""
from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, node): # O(1)
        self._data.append(node)

    def dequeue(self): # O(1)
        self._data.popleft()

    def not_empty(self):
        return bool(len(self._data))

"""
HashTable
    insert 
    delete
    search
        average: O(1)
        worst: O(n)
"""
