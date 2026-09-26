from arvore_binaria import ArvoreBinariaBusca
 
arvore_espera = ArvoreBinariaBusca()
 
 
def popular_arvore_da_lista(lista_encadeada):
    """Percorre a lista encadeada e insere todos os cadastros na arvore binaria."""
    atual = lista_encadeada.inicio
    while atual:
        arvore_espera.inserir(atual.nome, atual.idade, atual.telefone, atual.cidade)
        atual = atual.proximo
 
 
def buscar(nome):
    return arvore_espera.buscar(nome)
 
 
def alterar_nome(nome_antigo, novo_nome):
    p = arvore_espera.buscar(nome_antigo)
    if not p:
        return False
    idade, telefone, cidade = p.idade, p.telefone, p.cidade
    arvore_espera.remover(nome_antigo)
    arvore_espera.inserir(novo_nome, idade, telefone, cidade)
    return True
 
 
def alterar_idade(nome, nova_idade):
    p = arvore_espera.buscar(nome)
    if p:
        p.idade = nova_idade
        return True
    return False
 
 
def alterar_telefone(nome, novo_tel):
    p = arvore_espera.buscar(nome)
    if p:
        p.telefone = novo_tel
        return True
    return False
 
 
def descadastrar(nome):
    p = arvore_espera.buscar(nome)
    if p:
        arvore_espera.remover(nome)
        return True
    return False
 
 
def obter_primeiro():
    return arvore_espera.minimo()
 
 
def obter_ultimo():
    return arvore_espera.maximo()
 
 
def get_pessoas():
    """Retorna os registros em ordem para usar com o assistente depois."""
    return arvore_espera.em_ordem()