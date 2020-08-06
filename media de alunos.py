'''Tipo Booleano

Algebra Booleanam criada por George Boole

2 constantes Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiuscula

Errado:

true, false

Curto:

True, False
'''
nome = "aline spindola"
print(nome[0:5])

idade = 17

nota1 = int(input("digite a primeira nota do aluno(a): "))
nota2 = int(input("digite a segunda nota do aluno(a): "))
nota3 = int(input("digitea a terceira nota do aluno(a): "))
nota4 = int(input("digite a quarta nota do aluno(a): "))

media:float= (nota1+nota2+nota3+nota4)/4

print("a nota1 do aluno é {}, a nota2 do aluno é {}, a nota3 do aluno é {} e a nota 4 do aluno é {}"
    "por tanto, a média final do aluno será {}".format(nota1,nota2,nota3,nota4,media))

if media >= 5:
    print("hm, está na média, passou de ano")
elif media == 10:
    print("MEUS PARABÉNS, VOCÊ É UM GÊNIO")
else:
    print("reprovado(a), burro(a)")
