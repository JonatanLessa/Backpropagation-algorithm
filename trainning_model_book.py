import numpy as np
import math

learning_rate = 0.4
wanted = 0

def trainning_model_book(qtd, X_normalized, weight, bias, y_normalized, error_list):

    sum_neuron = np.zeros((qtd-1,1))
    neuron_output = np.zeros((qtd-1,1))        

    for i in range(len(X_normalized)):
        output_neuron_input = 0
        p = 0
        print(f'{i+1}/{len(X_normalized)}')
        #print(f'Weight list: {weight}, Bias List: {bias}')
        for a in range(qtd-1): 

            # Cálculo do somatório das entradas nos neurônios da camada oculta
            sum_neuron[a][0] = X_normalized[i][0] * weight[p][0] + X_normalized[i][1] * weight[p+1][0] 
            neuron_output[a][0] = 1 / (1 + math.exp(-(sum_neuron[a][0] + bias[a][0])))
            print(f'X_normalized{i}: {X_normalized[i][0]}, Weight[{p}]: {weight[p][0]}, X_normalized{i+1}: {X_normalized[i][1]}, Weight[{p+1}]: {weight[p+1][0]}, Bias[{a}]: {bias[a][0]}, Sum neuron[{a}]: {sum_neuron[a][0]}, Neuron output[{a}]: {neuron_output[a][0]}')
            p += 2
        #print(f'Neuron output list: {neuron_output}')
        # Cálculo do somatório das entradas no neurônio da camada saída
        for b in range(len(neuron_output)):
            output_neuron_input += neuron_output[b][0] * weight[p][0]  # Neuronio4    
            p += 1    
        print(f'Sum of inner layer neurons: {output_neuron_input}')
        neuron_output_final = 1 / (1 + math.exp(-(output_neuron_input + bias[a+1][0])))
        print(f'Neuron output final: {neuron_output_final}')
        
        print(f'    >>> y_normalized: {y_normalized[i]}')

        # Cálculo do erro do neurônio de saída
        error = wanted - neuron_output_final
        error_list.append(abs(error))  
        # Cálculo do valor da derivada da sigmóide e sigmóide do neurônio de saída
        
        deriv_neuro_saida = math.exp(-(output_neuron_input))/((1 + math.exp(-(output_neuron_input)))**2)
        sig_neuro_saida = neuron_output_final * deriv_neuro_saida

        weight_error_ocult = []
        deriv_neuro_list = []
        sig_neuro_list = []   
        for c in range(qtd-1):           
            weight_error_ocult.append(learning_rate * error * deriv_neuro_saida * neuron_output[c][0])
            deriv_neuro_list.append(math.exp(-(sum_neuron[c][0]))/((1 + math.exp(-(sum_neuron[c][0])))**2))
        print(f'Weight_error_ocult_list: {weight_error_ocult}')
        #print(f'Weight error list: {weight_error_ocult}') 
        # Cálculo dos ajustes de pesos dos arcos que ligam os neurônios da camada oculta ao neurônio de saida
        q = 0
        for d in range(qtd-1):
            q += 2 
        print(f'Lista Pesos: {weight}')       
        for d in range(qtd-1):
            weight[q][0] = weight[q][0] + weight_error_ocult[d]
            sig_neuro_list.append(deriv_neuro_list[d] * sig_neuro_saida * weight[q][0])
            print(f'deriv_neuro_list[{d}]: {deriv_neuro_list[d]}, sig_neuro_sainda: {sig_neuro_saida}, weight[{q}][0]: {weight[q][0]}')
            q +=1  
        print(f'deriv_neuro_lists: {deriv_neuro_list}')    
        print(f'Sigmoid neuron list: {sig_neuro_list}')        
        # Cálculo do ajuste do bias do neurônio de saída
        bias_error_out = learning_rate * error * deriv_neuro_saida * 1
        bias[-1][0] = bias[-1][0] + bias_error_out
        print(f'BiasErro: {bias_error_out}, bias_fim{bias[-1][0]}')
        # Cálculo dos ajustes de pesos dos arcos que ligam os neurônios da entrada aos neurônios da camada de oculta
        r = 0
        for e in range(qtd-1):
            r += 2
        s = 0
        print(f'Weight before: {weight}')
        for f in range(qtd-1): 
            weight[s][0] = weight[s][0] + weight[r][0] * 1 * sig_neuro_list[f]
            weight[s+1][0] = weight[s+1][0] + weight[r][0] * 1 * sig_neuro_list[f]
            bias[f][0] = bias[f][0] + weight[r][0] * 1 * sig_neuro_list[f]
            s += 2
            r += 1
        print(f'Weight after: {weight}')
        print(bias)            

    return weight, bias, error_list