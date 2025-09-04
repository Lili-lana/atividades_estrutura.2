# atividade_2.py
# arvore binaria de busca (bst) com inserção, busca, remoção, altura e profundidade
# visualização com graphviz

import random
from graphviz import Digraph

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # inserir um valor
    def insert(self, valor):
        if self.root is None:
            self.root = Node(valor)
        else:
            self._insert(self.root, valor)

    def _insert(self, node, valor):
        if valor < node.valor:
            if node.left is None:
                node.left = Node(valor)
            else:
                self._insert(node.left, valor)
        elif valor > node.valor:
            if node.right is None:
                node.right = Node(valor)
            else:
                self._insert(node.right, valor)

    # buscar um valor
    def search(self, valor):
        return self._search(self.root, valor)

    def _search(self, node, valor):
        if node is None:
            return False
        if node.valor == valor:
            return True
        elif valor < node.valor:
            return self._search(node.left, valor)
        else:
            return self._search(node.right, valor)

    # remover um valor
    def delete(self, valor):
        self.root = self._delete(self.root, valor)

    def _delete(self, node, valor):
        if node is None:
            return node
        if valor < node.valor:
            node.left = self._delete(node.left, valor)
        elif valor > node.valor:
            node.right = self._delete(node.right, valor)
        else:
            # caso 1: nó folha
            if node.left is None and node.right is None:
                return None
            # caso 2: nó com um filho
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # caso 3: nó com dois filhos
            else:
                sucessor = self._min_value_node(node.right)
                node.valor = sucessor.valor
                node.right = self._delete(node.right, sucessor.valor)
        return node

    def _min_value_node(self, node):
        atual = node
        while atual.left is not None:
            atual = atual.left
        return atual

    # calcular altura da arvore
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    # calcular profundidade de um nó
    def depth(self, valor):
        return self._depth(self.root, valor, 0)

    def _depth(self, node, valor, nivel):
        if node is None:
            return -1
        if node.valor == valor:
            return nivel
        elif valor < node.valor:
            return self._depth(node.left, valor, nivel + 1)
        else:
            return self._depth(node.right, valor, nivel + 1)

    # mostrar a arvore com graphviz
    def visualize(self, filename="tree"):
        dot = Digraph()
        if self.root:
            self._add_nodes(dot, self.root)
        dot.render(filename, format="png", cleanup=True)
        print(f"arvore gerada: {filename}.png")

    def _add_nodes(self, dot, node):
        if node.left:
            dot.edge(str(node.valor), str(node.left.valor))
            self._add_nodes(dot, node.left)
        if node.right:
            dot.edge(str(node.valor), str(node.right.valor))
            self._add_nodes(dot, node.right)


#testes e pipipi popopo
if __name__ == "__main__":
    # arvore com valores fixos
    print("==== arvore com valores fixos ====")
    valores = [55, 30, 80, 20, 45, 70, 90]
    bst = BinarySearchTree()
    for v in valores:
        bst.insert(v)
    bst.visualize("arvore_fixa")

    print("busca pelo valor 45:", bst.search(45))
    print("removendo o valor 30...")
    bst.delete(30)
    bst.visualize("arvore_fixa_removida")

    print("inserindo o valor 60...")
    bst.insert(60)
    bst.visualize("arvore_fixa_inserida")

    print("altura da arvore:", bst.height())
    print("profundidade do nó 45:", bst.depth(45))

    # arvore com valores aleatorios
    print("\n==== arvore com valores aleatorios ====")
    random_vals = random.sample(range(1, 200), 15)
    print("valores gerados:", random_vals)

    bst2 = BinarySearchTree()
    for v in random_vals:
        bst2.insert(v)
    bst2.visualize("arvore_randomica")

    print("altura da arvore aleatoria:", bst2.height())
