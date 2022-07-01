import numpy as np
import math


def trainning_model(qtd, X_normalized, weight, bias, y_normalized, error_list, learning_rate):

    sum_neuron = np.zeros((qtd-1,1))
    neuron_output = np.zeros((qtd-1,1))        

    for i in range(len(X_normalized)):
        output_neuron_input = 0
        p = 0
        print(f'{i+1}/{len(X_normalized)}')
        #print(f'Weight list: {weight}, Bias List: {bias}')
        for w in range(qtd-1): 

            # Cálculo do somatório das entradas nos neurônios da camada oculta
            sum_neuron[w][0] = X_normalized[i][0] * weight[p][0] + X_normalized[i][1] * weight[p+1][0] 
            neuron_output[w][0] = 1 / (1 + math.exp(-(sum_neuron[w][0] + bias[w][0])))
            print(f'X_normalized{i}: {X_normalized[i][0]}, Weight[{p}]: {weight[p][0]}, X_normalized{i+1}: {X_normalized[i][1]}, Weight[{p+1}]: {weight[p+1][0]}, Bias[{w}]: {bias[w][0]}, Sum neuron[{w}]: {sum_neuron[w][0]}, Neuron output[{w}]: {neuron_output[w][0]}')
            p += 2
        #print(f'Neuron output list: {neuron_output}')
        # Cálculo do somatório das entradas no neurônio da camada saída
        for z in range(len(neuron_output)):
            output_neuron_input += neuron_output[z][0] * weight[p][0]  
            p += 1    
        print(f'Sum of inner layer neurons: {output_neuron_input}')
        neuron_output_final = 1 / (1 + math.exp(-(output_neuron_input + bias[w+1][0]))) # Neurônio de saída
        print(f'Neuron output final: {neuron_output_final}')
        
        print(f'    >>> y_normalized: {y_normalized[i]}')

        # Cálculo do erro   
        error = y_normalized[i] - neuron_output_final   
       
        print(f'    >>> Erro : {error}')

        q = 0
        for a in range(qtd-1):
            q += 2

        weight_error = []
        for b in range(qtd-1):           
            weight_error.append(weight[q][0] * error)
            q += 1
        #print(f'Weight error list: {weight_error}')  

        r = 0
        for c in range(qtd-1): 
            weight[r][0] = weight[r][0] + learning_rate * weight_error[c] * (math.exp(-(X_normalized[i][0]))) / (1 + math.exp(-(X_normalized[i][0])))**2 * X_normalized[i][0]
            weight[r+1][0] = weight[r+1][0] + learning_rate * weight_error[c] * (math.exp(-(X_normalized[i][1]))) / (1 + math.exp(-(X_normalized[i][1])))**2 * X_normalized[i][1]
            r += 2
        for d in range(qtd-1):
            weight[r][0] = weight[r][0] + learning_rate * error * (math.exp(-(neuron_output[d][0]))) / (1 + math.exp(-(neuron_output[d][0])))**2 * neuron_output[d][0]
            r += 1
        for e in range(qtd-1):
            bias[e][0] = bias[e][0] + learning_rate * weight_error[e] * (math.exp(-(neuron_output[e][0]))) / (1 + math.exp(-(neuron_output[e][0])))**2 * neuron_output[e][0]
        bias[-1][0] = bias[-1][0] + learning_rate * error * (math.exp(-(neuron_output[-1][0]))) / (1 + math.exp(-(neuron_output[-1][0])))**2 * neuron_output[-1][0]
        #print(f'Weight list: {weight}')
        #print(f'Bias list: {bias}')
    print('\n')    
    error_list.append(abs(error)) 
    return weight, bias, error_list