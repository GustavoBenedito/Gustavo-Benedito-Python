"""Crie uma classe para representar uma pessoa, com os
atributos privados de nome, idade e altura. Crie os métodos públicos necessários para
sets e gets e também um método para imprimir os dados de uma pessoa."""

"""
class Funcionario:
    def __init__(self, nome, cargo, idade, salario):
        self.nome = nome
        self.cargo = cargo
        self.idade = idade
        self.salario = salario
        self.bonus = 0

    def salario_final(self):
        self.salariobruto = self.salario + (self.salario * self.bonus)
        return round(self.salariobruto)


    @property
    def salario(self):
        return self._salariofinal
"""


class Funcionario:

    def __init__(self, nome, cpf, salario, salariofinal):

        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.salariofinal = salariofinal
        pass

    def calculo_bonus(self):
        if self.salario >= 1500:
            self.salariofinal = self.salario + (self.salario * 0.20)
        else:
            self.salariofinal = self.salario + (self.salario * 0.10)


# Andre = Funcionario("André", "1500", "1000")
Funcionario.nome = "André"
print(Funcionario.nome)
