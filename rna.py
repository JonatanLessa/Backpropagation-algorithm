import numpy as np
from desnormalize_data import desnormalize_x, desnormalize_y
from trainning_model import trainning_model
from trainning_model_book import trainning_model_book
from test_model import test
from normalize_data import normalize
from weight_raffle import weight_raffle, bias_raffle
import matplotlib.pyplot as plt

DATA =  'D:/Dropbox/IFAL-SI/8_Periodo/Sistemas de Apoio à Decisão/Backpropagation-algorithm/housing_data.csv'
# district_cod, area, iptu, condominium_value, bedrooms, bathrooms, value
dataset = np.loadtxt(DATA, delimiter=',')
# area, condominium_value
X = dataset[:,1:3]
# value
y = dataset[:,6]
#print(dataset)

normalized = np.zeros((dataset.shape))

new_data = normalize(dataset, normalized)
X_normalized = new_data[:,1:3]
y_normalized = new_data[:,5]
print(len(X))
#print(y)

# Quantidade de neurônios
qtd = 20   
weight = weight_raffle(qtd)
#print(f'Lista de pesos: {weight}')

bias = bias_raffle(qtd)
#print(f'Lista de bias: {bias}')

count_epoch = 1
# Quantidade de épocas
epoch = 100
learning_rate = 0.4

error_list = []

# Trainnig
while count_epoch <= epoch:
    
    print(f'Epoch: {count_epoch}/{epoch}')    
    weight, bias, error_list = trainning_model(qtd, X_normalized, weight, bias, y_normalized, error_list, learning_rate)
    #weight, bias, error_list = trainning_model_book(qtd, X_normalized, weight, bias, y_normalized, error_list)
    #print(f'Final Weitgh: {weight}, Final Bias: {bias}')
    count_epoch += 1  

# Testing
new_y = test(qtd, X_normalized, weight, bias, y_normalized)

X_desnormalized = np.zeros((X_normalized.shape))  
y_desnormalized = np.zeros((y.shape))

X_desnormalized = desnormalize_x(X, X_normalized, X_desnormalized)
#print(X_desnormalized)
y_desnormalized = desnormalize_y(y, new_y, y_desnormalized)
#print(y_desnormalized)

print(f'        >>> y real:      {y}')
print(f'        >>> y previsto:  {y_desnormalized}')

precos_previstos = y_desnormalized
precos_reais = y
print(len(error_list))
print(error_list)

#formatter = ('{:.0f}'.format())
fig, ax = plt.subplots(ncols=2, nrows=1, figsize=(12, 6))
fig.suptitle(f'Gráfico de Resultados - Neurônios: {qtd}, Taxa de Aprendizagem: {learning_rate}, Épocas: {count_epoch-1}', size=20)
#ax[0].yaxis.set_major_formatter(formatter)
ax[0].plot(precos_reais, color='blue', label='Preço real')
ax[0].plot(precos_previstos, color='red', label='Preço previsto')
ax[0].set_title('Modelo preditivo')
ax[0].set_xlabel('Entradas')
ax[0].set_ylabel('Preço')
ax[0].legend()
ax[1].plot(error_list)
ax[1].set_title('Taxa de erro')
ax[1].set_xlabel('Épocas')
ax[1].set_ylabel('Taxa de erro')

plt.show()