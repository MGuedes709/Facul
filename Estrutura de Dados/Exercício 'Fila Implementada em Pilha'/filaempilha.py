class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if self.is_full():
            print("Error: Stack overflow")
        else:
            self.top += 1
            self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            print("Error: Stack underflow")
            return None
        else:
            item = self.stack[self.top]
            self.top -= 1
            return item

class Queue:
    def __init__(self):
        self.stack1 = Stack(100)
        self.stack2 = Stack(100)
        self.count = 0

    def enqueue(self, data):
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())
        self.stack1.push(data)
        self.count += 1

    def dequeue(self):
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        if not self.stack2.is_empty():
            self.count -= 1
            return self.stack2.pop()
        else:
            print("Pilha está vazia")
            return None

    def display(self):
        print("Elementos na pilha:")
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        while not self.stack2.is_empty():
            item = self.stack2.pop()
            print(item)
            self.stack1.push(item)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()
queue.dequeue()
queue.display()
