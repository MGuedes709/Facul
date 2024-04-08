class Node:
    def __init__(self, data):
        # Inicializa um nó com o dado fornecido
        self.data = data
        # Inicializa o ponteiro para o próximo nó como None
        self.next = None

class Stack:
    def __init__(self):
        # Inicializa a pilha com o topo como None e o tamanho como 0
        self.top = None
        self.size = 0

    def is_empty(self):
        # Verifica se a pilha está vazia
        return self.top is None

    def push(self, data):
        # Adiciona um novo nó com o dado fornecido no topo da pilha
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        # Incrementa o tamanho da pilha
        self.size += 1

    def pop(self):
        # Remove e retorna o dado do nó no topo da pilha
        if self.is_empty():
            print("Erro: Pilha vazia.")
            return None
        else:
            data = self.top.data
            self.top = self.top.next
            # Decrementa o tamanho da pilha
            self.size -= 1
            return data

    def peek(self):
        # Retorna o dado do nó no topo da pilha sem removê-lo
        if self.is_empty():
            print("Erro: Pilha vazia.")
            return None
        else:
            return self.top.data

    def display(self):
        # Exibe os elementos na pilha
        current = self.top
        if self.is_empty():
            print("Pilha vazia.")
        else:
            print("Elementos na pilha:")
            while current is not None:
                print(current.data)
                current = current.next
    
def decimal_para_binario(num_decimal, stack):
    if num_decimal < 0:
        # Verifica se o número é negativo e retorna um erro
        print("Erro: Número negativo.")
        return None
    else:
        if num_decimal == 0:
            stack.push(0)

        while num_decimal > 0:
            # Converte o número decimal para binário e armazena na pilha
            resto = num_decimal % 2
            stack.push(resto)
            num_decimal //= 2

        num_binario = ""
        while not stack.is_empty():
            # Monta o número binário a partir dos valores na pilha
            num_binario += str(stack.pop())

        return num_binario

stack = Stack()

numero_decimal = 25
numero_binario = decimal_para_binario(numero_decimal, stack)
print(f"O número binário equivalente de {numero_decimal} é: {numero_binario}")
