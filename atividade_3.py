# atividade_3.py
# arvore binaria com travessias: inorder, preorder e postorder
# visualização com graphviz

import random
from graphviz import Digraph

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # inserir valor na arvore (mesma ideia da bst)
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

    # inorder: esquerda - raiz - direita
    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.valor] + self._inorder(node.right)

    # preorder: raiz - esquerda - direita
    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        if node is None:
            return []
        return [node.valor] + self._preorder(node.left) + self._preorder(node.right)

    # postorder: esquerda - direita - raiz
    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node):
        if node is None:
            return []
        return self._postorder(node.left) + self._postorder(node.right) + [node.valor]

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


# ----------------- testes -----------------
if __name__ == "__main__":
    # arvore com valores fixos
    print("==== arvore com valores fixos ====")
    valores = [55, 30, 80, 20, 45, 70, 90]
    arvore_fixa = BinaryTree()
    for v in valores:
        arvore_fixa.insert(v)
    arvore_fixa.visualize("arvore_fixa_travessia")

    print("inorder:", arvore_fixa.inorder())
    print("preorder:", arvore_fixa.preorder())
    print("postorder:", arvore_fixa.postorder())

    # arvore com valores aleatorios
    print("\n==== arvore com valores aleatorios ====")
    random_vals = random.sample(range(1, 200), 10)
    print("valores gerados:", random_vals)

    arvore_randomica = BinaryTree()
    for v in random_vals:
        arvore_randomica.insert(v)
    arvore_randomica.visualize("arvore_randomica_travessia")

    print("inorder:", arvore_randomica.inorder())
    print("preorder:", arvore_randomica.preorder())
    print("postorder:", arvore_randomica.postorder())
