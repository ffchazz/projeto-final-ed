import heapq
 
 
class Grafo:
    def __init__(self):
        self.adj = {}
 
    def adicionar_aresta(self, u, v, peso):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        # Grafo nao-direcionado: aresta nos dois sentidos
        self.adj[u].append((v, peso))
        self.adj[v].append((u, peso))
 
    def dijkstra(self, origem, destino):
        """Retorna a menor distancia e a lista com o caminho percorrido."""
        if origem not in self.adj or destino not in self.adj:
            return float("inf"), []
 
        distancias = {v: float("inf") for v in self.adj}
        predecessores = {v: None for v in self.adj}
 
        distancias[origem] = 0
        fila = [(0, origem)]
 
        while fila:
            dist_atual, u = heapq.heappop(fila)
 
            if dist_atual > distancias[u]:
                continue
 
            if u == destino:
                break
 
            for vizinho, peso in self.adj[u]:
                nova_dist = dist_atual + peso
                if nova_dist < distancias[vizinho]:
                    distancias[vizinho] = nova_dist
                    predecessores[vizinho] = u
                    heapq.heappush(fila, (nova_dist, vizinho))
 
        caminho = []
        passo = destino
        while passo:
            caminho.append(passo)
            passo = predecessores[passo]
        caminho.reverse()
 
        if caminho and caminho[0] == origem:
            return distancias[destino], caminho
        return float("inf"), []