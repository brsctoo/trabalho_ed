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
        return a / b
    else:
        raise ValueError("Operador inválido")


print(f"O resultado de: 75.25.+9.12.+32.-* foi: \n{calcular_operacao('75.25.+9.12.+32.-*')}")