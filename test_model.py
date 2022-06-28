import numpy as np
import math

def test(qtd, X, weight, bias, y):

    sum_neuron = np.zeros((qtd-1,1))
    neuron_output = np.zeros((qtd-1,1))   
    new_y = np.zeros((y.shape))

    for i in range(len(X)):
        output_neuron_input = 0
        p = 0
        print(f'{i+1}/{len(X)}')
        #print(f'Weight list: {weight}, Bias List: {bias}')
        for w in range(qtd-1): 

            # Cálculo do soma_neurotório net weight * entrada
            sum_neuron[w][0] = X[i][0] * weight[p][0] + X[i][1] * weight[p+1][0] 
            neuron_output[w][0] = 1 / (1 + math.exp(-(sum_neuron[w][0] + bias[w][0])))
            print(f'X{i}: {X[i][0]}, Weight[{p}]: {weight[p][0]}, X{i+1}: {X[i][1]}, Weight[{p+1}]: {weight[p+1][0]}, Bias[{w}]: {bias[w][0]}, Sum neuron[{w}]: {sum_neuron[w][0]}, Neuron output[{w}]: {neuron_output[w][0]}')
            p += 2
        print(f'Neuron output list: {neuron_output}')
        for z in range(len(neuron_output)):
            output_neuron_input += neuron_output[z][0] * weight[p][0]  # Neuronio4    
            p += 1    
        print(f'Sum of inner layer neurons: {output_neuron_input}')
        neuron_output_final = 1 / (1 + math.exp(-(output_neuron_input + bias[w+1][0])))

        print(f'    Real value of y: {y[i]}')   
        print(f'    Output value: {neuron_output_final}')

        print(f'    >>> y: {y[i]}')

        new_y[i] = neuron_output_final
    
    return new_y