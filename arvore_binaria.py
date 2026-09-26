class NoArvore:
    def __init__(self, nome, idade, telefone, cidade):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cidade = cidade
        self.esquerda = None
        self.direita = None
 
 
class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
 
    def inserir(self, nome, idade, telefone, cidade):
        novo = NoArvore(nome, idade, telefone, cidade)
        if not self.raiz:
            self.raiz = novo
        else:
            self._inserir_rec(self.raiz, novo)
 
    def _inserir_rec(self, atual, novo):
        if novo.nome.lower() < atual.nome.lower():
            if atual.esquerda is None:
                atual.esquerda = novo
            else:
                self._inserir_rec(atual.esquerda, novo)
        else:
            if atual.direita is None:
                atual.direita = novo
            else:
                self._inserir_rec(atual.direita, novo)
 
    def buscar(self, nome):
        atual = self.raiz
        while atual:
            if nome.lower() == atual.nome.lower():
                return atual
            elif nome.lower() < atual.nome.lower():
                atual = atual.esquerda
            else:
                atual = atual.direita
        return None
 
    def minimo(self):
        if not self.raiz:
            return None
        atual = self.raiz
        while atual.esquerda:
            atual = atual.esquerda
        return atual
 
    def maximo(self):
        if not self.raiz:
            return None
        atual = self.raiz
        while atual.direita:
            atual = atual.direita
        return atual
 
    def remover(self, nome):
        self.raiz = self._remover_rec(self.raiz, nome)
 
    def _remover_rec(self, no, nome):
        if no is None:
            return None
 
        if nome.lower() < no.nome.lower():
            no.esquerda = self._remover_rec(no.esquerda, nome)
        elif nome.lower() > no.nome.lower():
            no.direita = self._remover_rec(no.direita, nome)
        else:
            # Caso 1: sem filhos
            if no.esquerda is None and no.direita is None:
                return None
            # Caso 2: apenas um filho
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            # Caso 3: dois filhos (sucessor em-ordem: menor da subárvore direita)
            sucessor = no.direita
            while sucessor.esquerda:
                sucessor = sucessor.esquerda
            no.nome = sucessor.nome
            no.idade = sucessor.idade
            no.telefone = sucessor.telefone
            no.cidade = sucessor.cidade
            no.direita = self._remover_rec(no.direita, sucessor.nome)
        return no
 
    def em_ordem(self):
        elementos = []
        self._em_ordem_rec(self.raiz, elementos)
        return elementos
 
    def _em_ordem_rec(self, no, lista):
        if no:
            self._em_ordem_rec(no.esquerda, lista)
            lista.append(no)
            self._em_ordem_rec(no.direita, lista)