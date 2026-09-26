def menu_secretario():
    print("---------------- Olá, Secretário(a)! ----------------")
    while True:
        print("\nVocê deseja:")
        print("(1) Cadastrar nova pessoa na lista de espera.")
        print("(2) Consultar pessoa cadastrada.")
        print("(3) Ver quantidade de pessoas cadastradas.")
        print("(4) Finalizar execução.")
 
        op = input("Digite sua opção: ").strip()
 
        # Se for menor que 1 ou maior que 4, ignora e volta pro menu
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
 
 
if __name__ == "__main__":
    menu_secretario()