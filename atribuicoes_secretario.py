import random
from lista_encadeada import ListaEncadeada
 
lista_espera = ListaEncadeada()
 
# Carrega cidades unicas das duas primeiras colunas do CSV
cidades = []
with open("cidades_vizinhas.csv", "r", encoding="utf-8") as f:
    for linha in f:
        partes = linha.strip().split(";")
        if len(partes) >= 2:
            if partes[0]:
                cidades.append(partes[0].strip())
            if partes[1]:
                cidades.append(partes[1].strip())
cidades = list(set(cidades))
 
 
def cadastrar(nome, idade, telefone):
    cidade = random.choice(cidades)
    lista_espera.inserir(nome, idade, telefone, cidade)
    return nome, idade, telefone, cidade
 
 
def consultar(nome):
    return lista_espera.buscar(nome)
 
 
def quantidade():
    return lista_espera.tamanho()
 
 
def get_lista():
    return lista_espera