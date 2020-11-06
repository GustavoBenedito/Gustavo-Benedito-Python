"""aosdifnasodfin"""
a = 0
b = 0
decisao = ""
while not decisao == "sair":
    decisao = input("decisa entre calcular e sair: ")
    if decisao == "sair":
        print("obrigado por usar nossa calculadora")
        break
    if decisao == "calcular":
        calculadora = input("digite ai algum sinal de +, -, * ou /: ")
        if calculadora == "+":
            a = int(input("diga um valor para a: "))
            b = int(input("diga um valor para b: "))
            soma = a + b
            print(f' o valor do calculo é de {soma}')
        if calculadora == "-":
            a = int(input("diga um valor para a: "))
            b = int(input("diga um valor para b: "))
            subtracao = a - b
            print(f' o valor da calculo é de {subtracao}')
        if calculadora == "*":
            a = int(input("diga um valor para a: "))
            b = int(input("diga um valor para b: "))
            multiplicacao = a * b
            print(f' o valor da calculo é de {multiplicacao}')
        if calculadora == "/":
            a = int(input("diga um valor para a: "))
            b = int(input("diga um valor para b: "))
            divisao = a / b
            print(f' o valor da calculo é de {divisao}')
