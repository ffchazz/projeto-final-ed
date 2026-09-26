import atribuicoes_secretario as sec
import atribuicoes_diretor as diretor
import atribuicoes_assistente as assistente
 
 
def menu_secretario():
    print("---------------- Olá, Secretário(a)! ----------------")
    while True:
        print("\nVocê deseja:")
        print("(1) Cadastrar nova pessoa na lista de espera.")
        print("(2) Consultar pessoa cadastrada.")
        print("(3) Ver quantidade de pessoas cadastradas.")
        print("(4) Finalizar execução.")
 
        op = input("Digite sua opção: ").strip()
 
        if op not in ["1", "2", "3", "4"]:
            continue
 
        if op == "1":
            nome = input("Digite o nome da pessoa: ")
            idade = input("Digite a idade: ")
            tel = input("Digite o telefone: ")
            nome, idade, tel, cid = sec.cadastrar(nome, idade, tel)
            print(f"Nome: {nome} | Idade: {idade} | Telefone: {tel} | Cidade: {cid}")
 
        elif op == "2":
            nome = input("Digite o nome da pessoa: ")
            p = sec.consultar(nome)
            if p:
                print(f"Nome: {p.nome} | Idade: {p.idade} | Telefone: {p.telefone} | Cidade: {p.cidade}")
            else:
                print("Pessoa não cadastrada. Tem certeza que o nome está certo?")
 
        elif op == "3":
            print(f"São {sec.quantidade()} pessoas na lista de espera.")
 
        elif op == "4":
            print("Fim das atividades sob responsabilidade do(a) Secretário(a).")
            break
 
 
def menu_diretor():
    print("\n---------------- Olá, Diretor(a)! ----------------")
    while True:
        print("\nVocê deseja:")
        print("(1) Alterar nome, idade ou telefone de pessoa cadastrada.")
        print("(2) Descadastrar pessoa.")
        print("(3) Obter informações da primeira pessoa em ordem alfabética de nome.")
        print("(4) Obter informações da última pessoa em ordem alfabética de nome.")
        print("(5) Confirmar validade da lista de espera e finalizar execução.")
 
        op = input("Digite sua opção: ").strip()
 
        if op not in ["1", "2", "3", "4", "5"]:
            continue
 
        if op == "1":
            nome = input("Digite o nome da pessoa que você quer editar: ")
            p = diretor.buscar(nome)
            if not p:
                print("Pessoa não cadastrada. Tem certeza que o nome está certo?")
                continue
 
            print(f"Nome: {p.nome} | Idade: {p.idade} | Telefone: {p.telefone} | Cidade: {p.cidade}")
            campo = input("O que você quer editar? Digite 1 para nome, 2 para idade ou 3 para telefone: ").strip()
 
            if campo == "1":
                novo_nome = input("Digite o novo nome: ")
                diretor.alterar_nome(nome, novo_nome)
                print("Dados atualizados com sucesso.")
            elif campo == "2":
                nova_idade = input("Digite a nova idade: ")
                diretor.alterar_idade(nome, nova_idade)
                print("Dados atualizados com sucesso.")
            elif campo == "3":
                novo_tel = input("Digite o novo telefone: ")
                diretor.alterar_telefone(nome, novo_tel)
                print("Dados atualizados com sucesso.")
 
        elif op == "2":
            nome = input("Digite o nome da pessoa que você quer descadastrar: ")
            p = diretor.buscar(nome)
            if not p:
                print("Pessoa não cadastrada ou lista de espera vazia. Tem certeza que o nome da pessoa está certo?")
                continue
 
            print(f"Nome: {p.nome} | Idade: {p.idade} | Telefone: {p.telefone} | Cidade: {p.cidade}")
            confirma = input(f"Tem certeza que deseja descadastrar {p.nome}? Digite S ou N: ").strip().upper()
            if confirma == "S":
                diretor.descadastrar(p.nome)
                print(f"{p.nome} descadastrado(a) com sucesso.")
 
        elif op == "3":
            p = diretor.obter_primeiro()
            if p:
                print(f"Nome: {p.nome} | Idade: {p.idade} | Telefone: {p.telefone} | Cidade: {p.cidade}")
            else:
                print("Lista de espera vazia.")
 
        elif op == "4":
            p = diretor.obter_ultimo()
            if p:
                print(f"Nome: {p.nome} | Idade: {p.idade} | Telefone: {p.telefone} | Cidade: {p.cidade}")
            else:
                print("Lista de espera vazia.")
 
        elif op == "5":
            print("Fim das atividades sob responsabilidade do(a) Diretor(a).")
            break
 
 
def menu_assistente():
    print("\n---------------- Olá, Assistente! ----------------")
    while True:
        print("\nVocê deseja:")
        print("(1) Ver a menor distância entre a cidade da escola e a cidade de uma pessoa.")
        print("(2) Ver a menor distância da cidade da escola até a cidade da pessoa passando por uma cidade específica.")
        print("(3) Ver dados da(s) pessoa(s) que mora(m) na cidade mais perto da cidade da escola (incluindo distância).")
        print("(4) Finalizar execução.")
 
        op = input("Digite sua opção: ").strip()
 
        if op not in ["1", "2", "3", "4"]:
            continue
 
        if op == "1":
            nome = input("Digite o nome da pessoa cuja cidade te interessa: ")
            p, caminho, dist = assistente.menor_distancia_pessoa(nome)
            if not p:
                print("Pessoa não cadastrada ou lista de espera vazia. Tem certeza que o nome da pessoa está certo?")
            else:
                print(f"Nome: {p.nome} | Idade: {p.idade} | Telefone: {p.telefone} | Cidade: {p.cidade}")
                print(f"Menor caminho = {caminho} com custo {dist}")
 
        elif op == "2":
            nome = input("Digite o nome da pessoa cuja cidade te interessa: ")
            p, caminho, dist = assistente.menor_distancia_via_intermediaria(nome)
            if not p:
                print("Pessoa não cadastrada ou lista de espera vazia. Tem certeza que o nome da pessoa está certo?")
            else:
                print(f"Nome: {p.nome} | Idade: {p.idade} | Telefone: {p.telefone} | Cidade: {p.cidade}")
                print(f"Menor caminho = {caminho} com custo {dist}")
 
        elif op == "3":
            cidade, dist, moradores = assistente.moradores_cidade_mais_proxima()
            if not cidade:
                print("Lista de espera vazia.")
            else:
                print(f"A cidade mais próxima à cidade da escola que tem moradores na lista de espera (ver abaixo) é {cidade}. Distância = {dist}")
                for m in moradores:
                    print(f"Nome: {m.nome} | Idade: {m.idade} | Telefone: {m.telefone} | Cidade: {m.cidade}")
 
        elif op == "4":
            break
 
 
def main():
    # 1. Secretário (Lista Encadeada)
    menu_secretario()
 
    # Transição: Lista Encadeada -> Árvore BST
    diretor.popular_arvore_da_lista(sec.get_lista())
 
    # 2. Diretor (Árvore Binária de Busca)
    menu_diretor()
 
    # 3. Assistente (Grafo ponderado + Dijkstra)
    menu_assistente()
 
 
if __name__ == "__main__":
    main()