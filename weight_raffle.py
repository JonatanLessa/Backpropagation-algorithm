import numpy as np
import random


def weight_raffle(size):
    size = (size-1) * 3
    weights = np.zeros((size,1))
    # Atribuindo valores aleatórios para os pesos
    for i in range(len(weights)):
        weights[i][0] = random.randint(-2,2)
    
    return weights

def bias_raffle(size):
    bias = np.zeros((size,1))
    # Atribuindo valores aleatórios para os bias
    for i in range(len(bias)):
        bias[i][0] = random.randint(-2,2)

    return bias