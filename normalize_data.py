
# Normalizando dados 
def normalize(data, normalized):    

    for x in range(len(data)):
        for z in range(len(data[x])):     
            normalized[x][z] = (data[x][z] - data.min(axis=0)[z]) / (data.max(axis=0)[z] - data.min(axis=0)[z])

    return normalized
