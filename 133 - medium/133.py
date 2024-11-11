
from collections import deque

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        # Criando dict de acordo com a lista de adjacencia
        nodes = {}
        visitado = set()
        fila = deque()
        fila.append(node)
        while fila:
            tmp = fila.popleft()
            if tmp in visitado:
                continue
            visitado.add(tmp)
            nodes[tmp.val] = []
            for x in tmp.neighbors:
                nodes[tmp.val].append(x.val)
                fila.append(x)
 
        # 2. Construindo copia do grafo
        copied_nodes = {}
        for x in nodes:
            copied_nodes[x] = Node(x)

        # Copiando vizinhos
        for x in nodes:
            copied_nodes[x].neighbors = []
            for neighbor in nodes[x]:
                copied_nodes[x].neighbors.append(copied_nodes[neighbor])


        return copied_nodes[node.val]
    
def adjacency_list_to_graph(adj_list):
    if not adj_list:
        return None
    
    # Criando dict para cada no
    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}

    # Conectando nos de acordo com a adjacencia
    for i, neighbors in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[neighbor] for neighbor in neighbors]

    # Retornando o primeiro no 
    return nodes[1]

def graph_to_adjacency_list(node):
    if not node:
        return []

    adjacency_list = {}
    visited = set()
    queue = deque([node])

    # Usando BFS para percorrer os nos
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)

        # Buscando vizinhos
        adjacency_list[current.val] = [neighbor.val for neighbor in current.neighbors]

        for neighbor in current.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)

    # Convertendo o grafo para lista de adjacencia
    max_val = max(adjacency_list.keys())
    adj_list_output = [adjacency_list.get(i, []) for i in range(1, max_val + 1)]
    return adj_list_output


solution = Solution()
# result = solution.cloneGraph(adjacency_list_to_graph([[2,4],[1,3],[2,4],[1,3]])) # Expected = [[2,4],[1,3],[2,4],[1,3]]
# result = solution.cloneGraph(adjacency_list_to_graph([[]])) # Expected = [[]]
result = solution.cloneGraph(adjacency_list_to_graph([])) # Expected = []
print(graph_to_adjacency_list(result))

        