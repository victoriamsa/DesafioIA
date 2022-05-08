def fitness(ind):
    conflicts = 0

    for i in range(len(ind)):
        for j in range(len(ind)):
            if i!=j:
                # Check same column conflict
                if ind[i] == ind[j]:
                    conflicts +=1
                
                # Check diagonal conflict 
                if abs(ind[i]-ind[j]) == abs(i-j):
                    conflicts +=1

    return -conflicts

def vizinhoaleatorio(list_rainhas):

    pos = -1
    conflitos = fitness(list_rainhas)
    novos_conflitos = conflitos + 1
    
    n = len(list_rainhas)
    for i in range(len(list_rainhas)):
        qtd = list_rainhas.count(list_rainhas[i])
        if qtd > 1 and pos != i:
            pos = i
            break
        else:
             while novos_conflitos > conflitos:
                rainha1 = np.random.randint(n)
                rainha2 = np.random.randint(n)
                aux1 = list_rainhas[rainha1]
                aux2 = list_rainhas[rainha2]
                list_rainhas[rainha2] = aux1
                list_rainhas[rainha1] = aux2         
                novos_conflitos = fitness(list_rainhas)
                return list_rainhas
    
    for i in range(len(list_rainhas)):
        if i not in list_rainhas:
            list_rainhas[pos] = i
            return list_rainhas    

   


    return list_rainhas
    


if __name__ == "__main__":
    import numpy as np
    
    # Iniciar a lista
    n = 30
    list_rainhas = [np.random.randint(n) for i in range(n)]
    # Analisar os conflitos da lista inicial
    conflitos = fitness(list_rainhas)

    # Iniciar o Loop
    n_iter = 10000

    for i in range(n_iter):
        if conflitos !=0:
            vizinho = vizinhoaleatorio(list_rainhas)
            # print(vizinho)
            conflitos_atual = fitness(vizinho)
            
            if conflitos_atual > conflitos:
                list_rainhas = vizinho
                conflitos = conflitos_atual
            #print(list_rainhas)
    print(list_rainhas, conflitos)