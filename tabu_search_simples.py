from random import randint

def solucao_inicial(tam):
    sol = [str(randint(0,1)) for i in range(tam)]
    return "".join(sol)
    
sol = solucao_inicial(4)

def fitness1(sol):
    return sol.count("1")


def gerar_vizinhos(sol):
    vizinhos = []
    for i in range(len(sol)):
        lista_bits = list(sol)
        if sol[i] == "0":
            lista_bits[i] = "1"
        else:
            lista_bits[i] = "0"
        vizinho = "".join(lista_bits)
        vizinhos.append(vizinho)
    
    return vizinhos

def movimento_tabu(sol,vizinho):
    for i in range(len(sol)):
        if sol[i] != vizinho[i]:
            return i

def obter_melhor_vizinho(vizinhos,lista_tabu,melhor_sol,sol):
    vizinhos.sort(key=fitness1, reverse = True)
    
    for vizinho in vizinhos:
        if movimento_tabu(sol,vizinho) in lista_tabu:
            if fitness1(vizinho) > fitness1(melhor_sol):
                return vizinho
        else:
            return vizinho
    
    print("erro")
    


def tabu_search(bits = 4,BTmax=2,T=1):
    lista_tabu =[]
    Iter = 0
    melhor_iter = 0
    sol = solucao_inicial(bits)
    melhor_sol  = sol[:]
    print("solução inicial:",sol)
    print("valor da solução inicial é:",fitness1(sol))
    
    while (Iter - melhor_iter) <= BTmax:
        avaliacao_sol = fitness1(sol)
        vizinhos = gerar_vizinhos(sol)
        melhor_vizinho = obter_melhor_vizinho(vizinhos,lista_tabu,melhor_sol,sol)
        sol = melhor_vizinho[:]
        pos_tabu =  movimento_tabu(sol,melhor_vizinho)
        
        if len(lista_tabu)<T:
            lista_tabu.append(pos_tabu)
        else:
            lista_tabu.pop(0)
            lista_tabu.append(pos_tabu)
        
        if fitness1(melhor_vizinho)>fitness1(melhor_sol):
            melhor_sol = melhor_vizinho[:]
            melhor_iter +=1
            
        Iter +=1
    return melhor_sol

print(tabu_search())
        
    

        

        
        
        