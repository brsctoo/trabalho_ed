"""
Implementação de um calculador de expressões em notação posfixa utilizando uma pilha.
A expressão é lida como uma string onde os números são separados por pontos (.) e os operadores são símbolos matemáticos (+, -, *, /).

Exemplo de uso:
    calcular_operacao("75.25.+9.12.+32.-*")
    retorna: -1100.0

    calcular_operacao("2.3.4.+5./*6.-")
    retorna: -3.2

Erros tratados:
- Divisão por zero
- Pilha vazia ao tentar desempilhar
- Pilha com mais de um elemento ao final da operação
- Operador inválido
"""

from pilha import Pilha

def calcular_operacao(exp: str) -> float:
    pilha = Pilha()
    num = ""
    operadores = {"+", "-", "*", "/"}

    for char in exp:
        if char != ".":
            if char in operadores:
                resultado = operar(char, pilha)
                pilha.empilha(resultado)
            else:
                num += char
        else:
            if num:
                pilha.empilha(float(num))
                num = ""
    
    if pilha.pilha_vazia():
        raise Exception("Pilha Vazia -> Não ocorreu operação")
    elif pilha.topo > 0:
        raise Exception("Pilha com mais de um elemento -> Operação incompleta")
    return pilha.desempilha()

def operar(operador: str, pilha: Pilha) -> float:
    b = pilha.desempilha()
    a = pilha.desempilha()
    
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        if b == 0:
            raise ValueError("Erro -> Divisão por zero")
        return a / b
    else:
        raise ValueError("Operador inválido")

