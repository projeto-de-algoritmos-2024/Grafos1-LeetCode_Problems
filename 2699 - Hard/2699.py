import heapq
from typing import List
from collections import defaultdict

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        # Inicializa o grafo e armazena as arestas
        graph = defaultdict(list)
        edge_data = []

        # Configura o grafo e armazena arestas com peso -1 em edge_data
        for index, (u, v, w) in enumerate(edges):
            if w != -1:
                graph[u].append((v, w))
                graph[v].append((u, w))
            edge_data.append((u, v, w, index))

        # Função para calcular a menor distância de source a destination
        def calculate_shortest_path():
            min_heap = [(0, source)]
            distances = [float('inf')] * n
            distances[source] = 0

            while min_heap:
                current_distance, node = heapq.heappop(min_heap)
                if current_distance > distances[node]:
                    continue
                for neighbor, weight in graph[node]:
                    new_distance = current_distance + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        heapq.heappush(min_heap, (new_distance, neighbor))
            return distances[destination]

        # Calcula a menor distância inicial sem modificar pesos
        shortest_initial_distance = calculate_shortest_path()

        # Se a distância inicial é menor que o alvo, retorna vazio; se é igual, ajusta pesos -1 para target + 1
        if shortest_initial_distance < target:
            return []
        if shortest_initial_distance == target:
            for u, v, w, idx in edge_data:
                if w == -1:
                    edges[idx][2] = target + 1
            return edges

        # Modifica pesos -1 para tentar alcançar a distância alvo
        for u, v, w, idx in edge_data:
            if w == -1:
                edges[idx][2] = 1  # Define peso inicial como 1
                graph[u].append((v, 1))
                graph[v].append((u, 1))
                
                # Calcula nova menor distância
                new_distance = calculate_shortest_path()

                # Se distância está próxima do alvo, ajusta o peso
                if new_distance <= target:
                    edges[idx][2] += target - new_distance
                    # Define os pesos restantes para target + 1
                    for uu, vv, ww, jdx in edge_data:
                        if edges[jdx][2] == -1:
                            edges[jdx][2] = target + 1
                    return edges

        # Se não foi possível alcançar a distância alvo, retorna vazio
        return []

# Selecione a forma de entrada desejada descomentando apenas uma das três opções

# Forma 1
# n = 5
# edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]
# source = 0
# destination = 1
# target = 5

# Forma 2
# n = 3
# edges = [[0,1,-1],[0,2,5]]
# source = 0
# destination = 2
# target = 6

# Forma 3
n = 4
edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]]
source = 0
destination = 2
target = 6

# Instancia a solução e executa a função
solution = Solution()
resultado = solution.modifiedGraphEdges(n, edges, source, destination, target)

# Exibe o resultado
print(resultado)
