
# Desnormalizando dados de X
def desnormalize_x(X, X_normalized, X_desnormalized):
    
    for x in range(len(X)):
        for z in range(len(X[x])):     
            X_desnormalized[x][z] = X_normalized[x][z] * (X.max(axis=0)[z] - X.min(axis=0)[z]) + X.min(axis=0)[z]
    #print(f'X desnormalizado: {X_desnormalized}')
    return X_desnormalized

# Desnormalizando dados de y 
def desnormalize_y(y, new_y, y_desnormalized): 
    
    for w in range(len(y)):
        y_desnormalized[w] = '{:.2}'.format(new_y[w] * (y.max() - y.min()) + y.min())
    return y_desnormalized