from grafo import Grafo
import atribuicoes_diretor as diretor
 
grafo = Grafo()
CIDADE_ESCOLA = "Guarujá"
CIDADE_INTERMEDIARIA = "Indaiatuba"
 
# Carrega o grafo a partir de cidades_vizinhas.csv
with open("cidades_vizinhas.csv", "r", encoding="utf-8") as f:
    for linha in f:
        partes = linha.strip().split(";")
        if len(partes) >= 3:
            c1 = partes[0].strip()
            c2 = partes[1].strip()
            peso = int(partes[2].strip())
            grafo.adicionar_aresta(c1, c2, peso)
 
 
def menor_distancia_pessoa(nome):
    p = diretor.buscar(nome)
    if not p:
        return None, None, None
    dist, caminho = grafo.dijkstra(CIDADE_ESCOLA, p.cidade)
    return p, caminho, dist
 
 
def menor_distancia_via_intermediaria(nome):
    p = diretor.buscar(nome)
    if not p:
        return None, None, None
 
    dist1, cam1 = grafo.dijkstra(CIDADE_ESCOLA, CIDADE_INTERMEDIARIA)
    dist2, cam2 = grafo.dijkstra(CIDADE_INTERMEDIARIA, p.cidade)
 
    if dist1 == float("inf") or dist2 == float("inf"):
        return p, [], float("inf")
 
    caminho_total = cam1 + cam2[1:]
    custo_total = dist1 + dist2
    return p, caminho_total, custo_total
 
 
def moradores_cidade_mais_proxima():
    pessoas = diretor.get_pessoas()
    if not pessoas:
        return None, None, []
 
    menor_dist = float("inf")
    cidade_mais_perto = None
 
    # Encontra qual a menor distancia entre a escola e as cidades dos cadastrados
    for p in pessoas:
        dist, _ = grafo.dijkstra(CIDADE_ESCOLA, p.cidade)
        if dist < menor_dist:
            menor_dist = dist
            cidade_mais_perto = p.cidade
 
    # Seleciona todas as pessoas que moram nessa cidade mais proxima
    moradores = [p for p in pessoas if p.cidade == cidade_mais_perto]
    return cidade_mais_perto, menor_dist, moradores