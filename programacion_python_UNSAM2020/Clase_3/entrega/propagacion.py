def queimar_a_esquerda(indice, fosforos):
    if indice > 0 and fosforos[indice - 1] != -1:
        fosforos[indice - 1] = 1

def queimar_a_direita(indice, fosforos):
    if indice < len(fosforos) - 1 and fosforos[indice + 1] != -1:
        fosforos[indice + 1] = 1

def propagar(fosforos):
    fosforos_queimados = fosforos.copy()
    for indice, fosforo in enumerate(fosforos):
        if fosforo == 1:
            queimar_a_esquerda(indice, fosforos_queimados)
            queimar_a_direita(indice, fosforos_queimados)
    if str(fosforos) == str(fosforos_queimados):
        return fosforos_queimados
    else:
        return propagar(fosforos_queimados)


fosforos = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
print(propagar(fosforos))

fosforos_2 = [0, 0, 0, 1, 0, 0]
print(propagar(fosforos_2))

## 

def propagate(ls):
    resp = revert_and_fill(revert_and_fill(ls))

    return resp

def revert_and_fill(ls):
    resp = ls[::-1]
    for i in range(1, len(ls)):
        if(resp[i-1] == 1 and resp[i] == 0):
            resp[i] = 1
    return resp


print(propagate([0, 1, 0, 0]) == [1, 1, 1 ,1])

print(propagate([0, 0, -1, 1]) == [0, 0,-1 ,1])

print(propagate([0, -1, 0, 1, -1, 1]) == [0, -1, 1, 1, -1 ,1])

print(propagate([0, -1, 1, 0, -1, 0, 0]) == [0, -1, 1, 1, -1, 0, 0])

## 

def propagar(lista):
    
    zeros = 0
    tam = int(len(lista))

    for i, j in enumerate(lista):
        if j==0:
            zeros+=1

    for z in range(zeros):    
        for i, j in enumerate(lista):
                
            if j == 0 and lista[i-1] == 1:
                if i > 0:
                    lista[i] = 1
                
            elif j == 0 and lista[i+1] == 1:
                if i < tam:
                    lista[i] = 1
            
    return lista
                
print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
print(propagar([0, 0, 0, 1, 0, 0]))
