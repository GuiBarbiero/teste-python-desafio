contas = []  # Lista para armazenar as contas
idConta = 1  # gerar de forma autonoma o id

# Função para criar uma nova conta
# no caso configurei meus valores iniciais meu nome cpf e etc
def criarconta(nome, cpf):
    global idConta
    conta = {
        "id": idConta,
        "nome": nome,
        "cpf": cpf,
        "saldo": 0.0  # Saldo inicial é 0
    }
    contas.append(conta)
    idConta += 1
    return conta
# Função para dar detalhes de minha conta
def exibirdetalhes(conta):
    return f"\n| ID: {conta['id']} | Nome: {conta['nome']} | CPF: {conta['cpf']} | Saldo Disponível: R${conta['saldo']:.2f} |\n"
# Metodo para depositar
def depositarvalor(conta, valor):
    if valor > 0:
        conta["saldo"] += valor
        return f"\nDepósito de R${valor:.2f} realizado com sucesso!"
    else:
        return "Valor inválido para depósito."
# Aqui é o metodo para sacar
def sacarvalor(conta, valor):
    if valor > conta["saldo"]:
        return "Saldo insuficiente para saque."
    elif valor > 0:
        conta["saldo"] -= valor
        return f"\nSaque de R${valor:.2f} realizado com sucesso!"
    else:
        return "Valor inválido para saque."
# Função para exibir o menu
def Menu():
    print("\n=====================================")
    print("|        Sistema Bancário           |")
    print("=====================================")
    print("| 1. Criar nova conta               |")
    print("| 2. Exibir detalhes da conta       |")
    print("| 3. Depositar                      |")
    print("| 4. Sacar                          |")
    print("| 5. Sair                           |")
    print("=====================================")
# Função para encontrar uma conta por ID
def encontrarconta(idConta):
    return next((conta for conta in contas if conta["id"] == idConta), None)
# Função para criar uma nova conta
def FazConta(contas):
    print("\n======= Criar Nova Conta =======")
    nome = input("Digite o nome do titular: ")
    cpf = input("Digite o CPF do titular: ")
    conta = criarconta(nome, cpf)
    print(f"Conta criada com sucesso! ID da conta: {conta['id']}")
    print("===============================")
# Função para exibir os detalhes de uma conta
def exibir(contas):
    print("\n======= Exibir Conta =======")
    idConta = int(input("Digite o ID da conta: "))
    conta = encontrarconta(idConta)
    if conta:
        print(exibirdetalhes(conta))  # Exibe detalhes da conta com saldo
    else:
        print("Conta não encontrada.")
    print("=============================")
# Função para realizar um depósito
def depositar(contas):
    print("\n======= Depósito =======")
    idConta = int(input("Digite o ID da conta: "))
    conta = encontrarconta(idConta)
    if conta:
        valor = float(input("Digite o valor para depósito: "))
        print(depositarvalor(conta, valor))
    else:
        print("Conta não encontrada.")
    print("========================")
# Função para realizar um saque
def sacar(contas):
    print("\n======= Saque =======")
    idConta = int(input("Digite o ID da conta: "))
    conta = encontrarconta(idConta)
    if conta:
        valor = float(input("Digite o valor para saque: "))
        print(sacarvalor(conta, valor))
    else:
        print("Conta não encontrada.")
    print("=======================")
# inicia minha interface do meu banco
def interface():
    while True:
        Menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            FazConta(contas)
        elif opcao == '2':
            exibir(contas)
        elif opcao == '3':
            depositar(contas)
        elif opcao == '4':
            sacar(contas)
        elif opcao == '5':
            print("\nEncerrando o programa... Até logo!")
            print("=====================================")
            break
        else:
            print("\nOpção inválida! Tente novamente.")
# inicia minha interface do meu banco
interface()
'''
Desafio interessante, meu código está detalhado com oque cada parte faz, optei em não usar self ou init por questão de entendimento
alem de poder usar main ao final para iniciar minha interface.
optei em usar listas e não banco de dados por questões de verbosidade e complexidade de código.
Nos outros testes coloquei um comentario sobre função next() e usei ela nesse código tambem como exemplo.
Confesso que sem frameworks e bibliotecas tive um pouco de dificuldade, algo que seria interessante para ter algo mais visual seria usar
a biblioteca tkinter e tk para termos algo mais visual.
Espero ter atingido a expectativa e fico no aguardo de proximos passos.
'''
