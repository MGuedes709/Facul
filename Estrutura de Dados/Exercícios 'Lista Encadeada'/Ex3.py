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

        if current_node is None:
            pass  # A lista está vazia
        else:
            if current_node.data == value:
                self.head = current_node.next
            else:
            # Busca o nó anterior ao nó a ser removido
                while current_node.next is not None:
                    if current_node.next.data == value:
                        # Remove o nó com o valor especificado
                        current_node.next = current_node.next.next
                        break  # Encerra o loop após a remoção do nó
                    current_node = current_node.next

# Exemplo de uso

linked_list = LinkedList()
linked_list.append(53)
linked_list.append(2)
linked_list.append(3)
linked_list.append(9)
linked_list.append(4)

linked_list.print_list()  # Saída: 53 2 3 9 4

linked_list.remove(3)
linked_list.print_list()  # Saída: 53 2 9 4

linked_list.remove(53)  
linked_list.print_list()  # Saída:  2 9 4
