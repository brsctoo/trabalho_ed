"""
Implementação de um calculador de expressões em notação posfixa utilizando uma pilha.
A expressão é lida como uma string onde os números são separados por pontos (.) e os operadores são símbolos matemáticos (+, -, *, /).

Exemplo de uso:
    calcular_operacao("75.25.+9.12.+32.-*")
    retorna: -1100

    calcular_operacao("2.3.4.+5./*6.-")
    retorna: -3

Erros tratados:
- Divisão por zero
- Pilha vazia ao tentar desempilhar -> Falta operando
- Pilha com mais de um elemento ao final da operação -> Falta operadores
- Pilha vazia ao final da operação
- Operador inválido
"""

from pilha import Pilha
import sys
sys.stdout.reconfigure(encoding="utf-8")  # assegura saída UTF-8

def abrir_arquivo(nome_arquivo: str) -> str:
    with open(nome_arquivo, 'r') as arquivo:
        expressoes = arquivo.readlines()
        expressoes = [linha.strip() for linha in expressoes]
    return expressoes

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
    
    # Verifica se há exatamente um elemento na pilha ao final
    if pilha.pilha_vazia(): 
        raise Exception("Pilha vazia ao final da operação.")
    else:
        resultado = pilha.desempilha()
        if not pilha.pilha_vazia():
            raise Exception("Pilha não vazia após operação -> Falta operadores.")
            
    return resultado

def operar(operador: str, pilha: Pilha) -> float:

    if pilha.pilha_vazia():
        raise Exception("Pilha vazia ao tentar desempilhar para operação. -> Falta operando.")
    b = pilha.desempilha()
    if pilha.pilha_vazia():
        raise Exception("Pilha vazia ao tentar desempilhar para operação. -> Falta operando.")
    a = pilha.desempilha()
    
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        if b == 0:
            raise Exception("Divisão por zero")
        return a // b
    else:
        raise Exception("Operador inválido")
    
def main(arquivo: str) -> None:

    expressoes: list[str] = abrir_arquivo(arquivo)
    for expressao in expressoes:
        print(f"Calculando expressao posfixa: {expressao}")
        try:   
            resultado = int(calcular_operacao(expressao))
            print(f"Resultado da expressão: {resultado}\n")
        except Exception as e:
            print(f"Erro ao calcular a expressão: {e}\n")

if __name__ == "__main__":
    try:
        arquivo = input("Digite o arquivo com as expressões posfixas: ")
        main(arquivo)
    except Exception as e:
        print(f"Erro: {e}")