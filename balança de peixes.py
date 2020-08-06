nome = input("digite o nome do usuario: ")

peso = int(input("digite aqui o peso do peixe: "))
taxa = 4.00
if peso > 50:
    print("Senhor(a) {}, o peso do peixe não pode ultrapassar os 50Kg, você receberá uma multa de R$4,00 por Kg".format(nome))
    a = (peso - 50)*taxa
    multa = a + peso
    print ("a sua multa será de {}".format(multa))
else:
    print("o seu peixe não ltrapassou o limite, o valor a ser pago será de: R${},00".format(peso))