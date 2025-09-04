"""
Atv 1 - Árvores de expressões matemáticas
objetivo:
- criar e mostrar uma árvore fixa e aleatória de expressão matemática
- Lívia Lana 211332
"""

from graphviz import Digraph
import random

class No:
    def __init__(self, valor, esquerdo=None, direito=None):
        self.valor = valor
        self.esquerdo = esquerdo
        self.direito = direito

# função para desenhar a árvore
def desenhar_arvore(raiz, nome_arquivo="arvore"):
    dot = Digraph()

    def adicionar(no, pai=None):
        if no is None:
            return

        # cada nó vai ser identificado pelo seu valor e posição na memória
        id_no = str(id(no))
        dot.node(id_no, str(no.valor))

        if pai:
            dot.edge(pai, id_no)

        adicionar(no.esquerdo, id_no)
        adicionar(no.direito, id_no)

    adicionar(raiz)
    dot.render(nome_arquivo, format="png", cleanup=True)
    print(f"Árvore salva em {nome_arquivo}.png")

# fazer a árvore fixa
# Expressão: ((7 + 3) * (5 - 2)) / (10 * 20)
def arvore_fixa():
    esquerda = No("*",
                  No("+", No(7), No(3)),
                  No("-", No(5), No(2)))
    direita = No("*", No(10), No(20))
    raiz = No("/", esquerda, direita)
    return raiz

# 2) criar árvore aleatória
def gerar_expressao_aleatoria():
    operadores = ["+", "-", "*", "/"]
    numeros = [str(random.randint(1, 9)) for _ in range(4)]

    op1 = random.choice(operadores)
    op2 = random.choice(operadores)
    op3 = random.choice(operadores)

    # Ex: (a op1 b) op2 (c op3 d)
    return f"(({numeros[0]} {op1} {numeros[1]}) {op2} ({numeros[2]} {op3} {numeros[3]}))"


def construir_arvore(expr):
    tokens = expr.replace("(", " ( ").replace(")", " ) ").split()

    def parse():
        token = tokens.pop(0)
        if token == "(":
            esquerdo = parse()
            operador = tokens.pop(0)
            direito = parse()
            tokens.pop(0)  # remove ")"
            return No(operador, esquerdo, direito)
        else:
            return No(token)

    return parse()


# parte principal
if __name__ == "__main__":
    # Árvore fixa
    raiz_fixa = arvore_fixa()
    desenhar_arvore(raiz_fixa, "arvore_fixa")

    # Árvore aleatória
    expr = gerar_expressao_aleatoria()
    print("Expressão aleatória:", expr)
    raiz_aleatoria = construir_arvore(expr)
    desenhar_arvore(raiz_aleatoria, "arvore_aleatoria")
