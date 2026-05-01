agenda = {}

def adicionar_contato(agenda, nome, telefone):
    agenda[nome] = telefone
    print("Contato salvo")

def buscar_telefone(agenda, nome):
    if nome in agenda:
        print("Telefone:", agenda[nome])
    else:
        print("Contato não encontrado")

def remover_contato(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        print("Contato removido")
    else:
        print("Contato não encontrado")

def listar_contatos(agenda):
    if agenda == {}:
        print("Agenda vazia")
    else:
        for nome in agenda:
            print(nome, "-", agenda[nome])


while True:
    print("\n1 - Adicionar")
    print("2 - Buscar")
    print("3 - Remover")
    print("4 - Listar")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        adicionar_contato(agenda, nome, telefone)

    elif opcao == "2":
        nome = input("Nome: ")
        buscar_telefone(agenda, nome)

    elif opcao == "3":
        nome = input("Nome: ")
        remover_contato(agenda, nome)

    elif opcao == "4":
        listar_contatos(agenda)

    elif opcao == "5":
        print("Fim do programa")
        break

    else:
        print("Opção inválida")