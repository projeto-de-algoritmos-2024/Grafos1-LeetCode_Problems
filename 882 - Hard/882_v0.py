# Não é preciso montar o grafo com as subdivisões, afinal mesmo o grafo final 
# ele é bidirecional 
# a ideia é que apenas seja calculado o peso de cada "No Original"
# e se com esse peso é possível chegar com o valor que é inputado em M

from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def reachableNodes(self, edges, M, N):
        # Criando um Grafo vazio 

        # O grafo é um dict onde cada chave é um "No" e 
        # para chave vai ter uma lista de tuplas que são
        # os "Nos" adjancentes e seu nivel
        Grafo = defaultdict(set)

        # Criando a quantidade nos que vão ser inputadas (grafo original)
        distancia = [float('inf')] * N

        # Setando o no inicial como 0
        distancia[0] = 0
        
        # De acordo o que foi inputado vamos, montar o grafo com apenas os nos 
        # originais e seus pesos (w+1)
        # [[0,1,10],[0,2,1],[1,2,2]]
        arestas = edges
        for i, j, w in arestas:
            Grafo[i].add((j, w))
            Grafo[j].add((i, w))
            
        heap = [(0, 0)]

        while heap:
            min_distancia, idx = heappop(heap)
            for no_vizinho, custo in Grafo[idx]:
                cand = min_distancia + custo
                if cand < distancia[no_vizinho]:
                    distancia[no_vizinho] = cand
                    heappush(heap, (cand, no_vizinho)) 
                    
        reposta = 0

        # Somando o custo para chegar em determinado ponto de acordo com cada aresta 
        # que foi inputada
        for i, j, w in arestas:
            w1, w2 = M - distancia[i], M - distancia[j]
            reposta += (max(0, w1) + max(0, w2))
                
        return reposta
    

solution = Solution()
# result = solution.reachableNodes([[0,1,10],[0,2,1],[1,2,2]],6, 3,) # Expected = 13
# result = solution.reachableNodes([[0,1,4],[1,2,6],[0,2,8],[1,3,1]],10, 4,) # Expected = 23
result = solution.reachableNodes([[0,3,4],[2,3,1],[3,1,5],[0,2,2]],5, 4,) # Expected = 10
print(result)