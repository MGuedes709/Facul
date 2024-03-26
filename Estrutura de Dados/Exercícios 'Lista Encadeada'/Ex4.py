class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    def search(self, value):
        current_node = self.head
        while current_node:
            if current_node.data == value:
                return True
            current_node = current_node.next
        return False

    def insert(self, position, value):
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current_node = self.head
        for _ in range(position - 1):
            if current_node is None:
                raise IndexError("Index out of range")
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    def remove(self, value):
        current_node = self.head

        # Verifica se o valor a ser removido é o primeiro da lista
        if current_node is not None and current_node.data == value:
            self.head = current_node.next
            return

        # Busca o nó anterior ao nó a ser removido
        while current_node is not None:
            if current_node.next and current_node.next.data == value:
                break
            current_node = current_node.next

        # Remove o nó com o valor especificado, se encontrado
        if current_node is None or current_node.next is None:
            return
        current_node.next = current_node.next.next

    def count(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

# Exemplo de uso
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(20)
    linked_list.append(3)
    linked_list.append(11)
    linked_list.append(32)
    linked_list.append(9)

    print(linked_list.count())  # Saída: 6
