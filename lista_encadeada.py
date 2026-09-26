class No:
    def __init__(self, nome, idade, telefone, cidade):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cidade = cidade
        self.proximo = None
 
 
class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.qtd = 0
 
    def inserir(self, nome, idade, telefone, cidade):
        novo = No(nome, idade, telefone, cidade)
        if not self.inicio:
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo
        self.qtd += 1
 
    def buscar(self, nome):
        atual = self.inicio
        while atual:
            if atual.nome.strip().lower() == nome.strip().lower():
                return atual
            atual = atual.proximo
        return None
 
    def tamanho(self):
        return self.qtd