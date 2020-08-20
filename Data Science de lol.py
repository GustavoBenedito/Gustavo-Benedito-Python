import xlrd
import pandas as pd

partidas = pd.read_excel("C:/Users/gusta/OneDrive/Área de Trabalho/ProjetosPython/historico.xlsx")

# print(partidas)

# visualizar de uma linha até a outra use "alunosDF['Nome']"
# para visualizar uma linhacom condição faça "alunoDF.loc[alunosDF['idade']>18]"

# para mostrar uma linha exata use print(alunosDF.loc[alunosDF['idade']=="20"])
# manipulando o dataframe com loc gustavo = alunosDF.loc[alunosDF['nome']== 'Gustavo Benedito']
# print(partidas.head())

# vitorias = partidas["Vitoria/Derrota"]
# print(vitorias)

# excluir uma linha dados.drop('ID', axis = 1, inplace = True)


# HISTOGRAMA import matplotlib.pyplot as plt
# dados.hist(column = 'Age', bins=10)
#plt.show()

# import matplotlib.pyplot as plt 
# histograma = partidas.hist(column = 'Gold', bins = 100)
# plt.show()


# somentevitorias = partidas.loc[partidas['Vitoria/Derrota']=='Vitoria']
#somentevitorias = partidas.loc[partidas['Vitoria/Derrota']=='Vitória']
#print(somentevitorias)

faltantes = partidas.isnull().sum()
print(faltantes)
