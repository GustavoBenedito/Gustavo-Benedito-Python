"""Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual
de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse
ou iguale a população do país B, mantidas as taxas de crescimento. """

""" país A, 80000 habitantes, crescimento de 3%
 país B, 200000 habitantes, crescimento de 1.5% """

habitantesA = 800000
crescimentoA = 0.03

habitantesB = 2000000
crescimentoB = 0.015

anos = int(input("diga quanto tempo o país A demorará para alcançar o páis B: "))
simuladoA = habitantesA + ((habitantesA * crescimentoA)*anos)

if simuladoA != habitantesB:
    while simuladoA != habitantesB:
        anos = int(input("país A ainda não alcançou o páis B, tente novamente: "))
        simuladoA = habitantesA + ((habitantesA * crescimentoA) * anos)
        if simuladoA == habitantesB:
            print(("demorará {} para ter {} habitantes".format(anos, simuladoA)))
            break
else:
    print("demorará {} para ter {} habitantes".format(anos, simuladoA))
