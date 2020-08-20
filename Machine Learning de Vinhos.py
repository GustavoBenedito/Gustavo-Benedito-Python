import pandas as pd 
dadosDF = pd.read_csv("C:/Users/gusta/OneDrive/Área de Trabalho/ProjetosPython/DataSet.csv")
print(dadosDF.head(5))

dadosDF['style'] = dadosDF['style'].replace('red', 0)
dadosDF['style'] = dadosDF['style'].replace('white', 1)

print(dadosDF.head)

# Separando as variáveis entre preditoras e variável alvo
y = dadosDF['style']
x = dadosDF.drop('style', axis = 1)

from sklearn.model_selection import train_test_split

#criando os conjuntos de dados de treino e teste:

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3)
print(x_treino.shape)
print(y_treino.shape)

from sklearn.ensemble import ExtraTreesClassifier

#Criação do modelo:

modelo = ExtraTreesClassifier()
modelo.fit(x_treino,y_treino)

#imprimindo resultado:

resultado = modelo.score(x_teste, y_teste)
print("Acurácia de : ", resultado)

#testandoS

x_teste[400:403]
print(x_teste[400:403])

y_teste[400:403]
print('os vinhos e os dados pro computador adivinhar: ')
print(y_teste[400:403])

print("0 = Vinho Tinto, 1 = Vinho Seco")

previsoes = modelo.predict(x_teste[400:403])
print(f'o computador preve que os vinhos serão: {previsoes}')
print(f'Acurácia de: {resultado}%')