# Não é preciso montar o grafo com as subdivisões, afinal mesmo o grafo final 
# ele é bidirecional e os no subnos não vão ser usados 
# a ideia é que apenas seja calculado o peso de cada "No Original"
# e se com esse peso é possível chegar com o valor que é inputado em M
# Depois de verificado isso devemos ver se em cada aresta é possível chegar nela 
# pelas duas pontos e se for possível remover os nos intermediários que 
# estão sendo repetidos.
# Verificar a distancia de cada no original a partir de 0, depois somar 
# quando nos intermediários de cada aresta podem ser alcançados e por último 
# remover os nós que são contados mais de uma vez.

from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def reachableNodes(self, edges, M, N):
        # Criando um Grafo vazio
        Grafo = defaultdict(set)

        # Distancia de cada no do a partir de 0 inicialmente é infinita
        distancia = [float('inf')] * N

        # Setando a distancia do 0 para ele mesmo como 0
        distancia[0] = 0
        
        # De acordo o que foi inputado vamos, montar o grafo com apenas os nos 
        # originais e seus pesos (w+1), pois ele conta o no mesmo 
        # [[0,1,10],[0,2,1],[1,2,2]]
        arestas = edges
        for i, j, w in arestas:
            Grafo[i].add((j, w + 1))
            Grafo[j].add((i, w + 1))
        
        # Iniciando a partir do no 0 com distancia minima de 0
        heap = [(0, 0)]

        while heap:
            min_distancia, idx = heappop(heap)
            for no_vizinho, custo in Grafo[idx]:
                cand = min_distancia + custo
                if cand < distancia[no_vizinho]:
                    distancia[no_vizinho] = cand
                    heappush(heap, (cand, no_vizinho)) 

        # Com base na distancia minima, contamos quantos no do Grafo original 
        # podemos alcancar a partir do zeoro com o numero de movimentos (M)
        reposta = sum(distancia[i] <= M for i in range(N))
        
        # Agora para cada aresta é preciso verificar quais nos sao alcançaveis 
        # calculando subtraindo a distancia de cada Vertice do numero de movimentos 
        # e com os movimentos restantes podemos chegar nos "nos" que estão na arestra
        for i, j, w in arestas:
            w1, w2 = M - distancia[i], M - distancia[j]
            reposta += (max(0, w1) + max(0, w2))
            # Aqui precisamos subtrair do total os nos intermediários que podem chegar 
            # pelas duas pontas, ou seja estão sendo contatos repetidas vezes 
            if w1 >= 0 and w2 >= 0: reposta -= max(w1 + w2 - w, 0)
                
        return reposta
    

solution = Solution()
result = solution.reachableNodes([[0,1,10],[0,2,1],[1,2,2]],6, 3,) # Expected = 13
# result = solution.reachableNodes([[0,1,4],[1,2,6],[0,2,8],[1,3,1]],10, 4,) # Expected = 23
# result = solution.reachableNodes([[0,3,4],[2,3,1],[3,1,5],[0,2,2]],5, 4,) # Expected = 10
print(result)