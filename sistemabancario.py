contas = {}
TAXA_SAQUE = 2.5
TAXA_DEPOSITO = 1.0
TAXA_TRANSFERENCIA = 3.0
conta_logada = 0

def cadastrar(nome, senha, cpf, datadenascimento):
    idconta = hash(nome+senha+cpf+datadenascimento)
    codigo = hash(nome+senha)
    contas[codigo] = {
        "nome": nome,
        "senha": senha,
        "cpf": cpf,
        "datadenascimento": datadenascimento,
        "id_conta": idconta,
        "dinheiro": 0
    }

def login(nome, senha):
    global conta_logada
    codigo = hash(nome+senha)
    if codigo in contas:
        conta_logada = codigo
        print("Conta existente!")
    else:
        print("Conta não encontrada.")

def listar_saldo(codigo):
    if codigo in contas:
        print(f"Saldo atual: R${contas[codigo]['dinheiro']:.2f}")
    else:
        print("Conta não encontrada.")

def sacar(codigo, valor):
    if codigo in contas:
        total = valor + TAXA_SAQUE
        if contas[codigo]['dinheiro'] >= total:
            contas[codigo]['dinheiro'] -= total
            print(f"Saque de R${valor:.2f} realizado. Taxa: R${TAXA_SAQUE:.2f}")
            listar_saldo(codigo)
        else:
            print("Saldo insuficiente para saque e taxa.")
    else:
        print("Conta não encontrada.")

def depositar(codigo, valor):
    if codigo in contas:
        if valor > TAXA_DEPOSITO:
            contas[codigo]['dinheiro'] += (valor - TAXA_DEPOSITO)
            print(f"Depósito de R${valor:.2f} realizado. Taxa: R${TAXA_DEPOSITO:.2f}")
            listar_saldo(codigo)
        else:
            print("Valor insuficiente para cobrir a taxa de depósito.")
    else:
        print("Conta não encontrada.")

def transferir(codigo_origem, codigo_destino, valor):
    if codigo_origem in contas and codigo_destino in contas:
        total = valor + TAXA_TRANSFERENCIA
        if contas[codigo_origem]['dinheiro'] >= total:
            contas[codigo_origem]['dinheiro'] -= total
            contas[codigo_destino]['dinheiro'] += valor
            print(f"Transferência de R${valor:.2f} realizada. Taxa: R${TAXA_TRANSFERENCIA:.2f}")
            listar_saldo(codigo_origem)
        else:
            print("Saldo insuficiente para transferência e taxa.")
    else:
        print("Conta de origem ou destino não encontrada.")


while True:
    if conta_logada == 0:
        print(" Seja Bem-Vindo!")
        print(" Digite 1 para Cadastrar")
        print(" Digite 2 para fazer um login")
        print(" Digite 3 para Sair")
        escolha = int(input(" O que deseja fazer?"))
        if escolha == 1:
            nome = input(" Insira seu nome:")
            senha = input(" Crie sua Senha:")
            cpf = input(" Insira seu CPF:")
            datadenascimento = input(" Insira sua data de nacimento:")
            cadastrar(nome,senha,cpf,datadenascimento)
        elif escolha == 2:
            nome = input(" Digite o nome: ")
            senha = input(" Digite a senha: ")
            login(nome, senha)
        elif escolha == 3:
            print(" Você saiu")
            quit()
    else:
        print(f"Bem vindo {contas[conta_logada]['nome']}")
        print(" Qual ação deseja realizar agora?")
        print(" Se deseja sacar digite 1")
        print(" Se deseja depósito digite 2.")
        print(" Se deseja realizar uma tranferência digite 3.")
        print(" Se deseja consultar o saldo digite 4.")
        print(" Digite 5 para sair da conta")
        escolha = int(input(" O que deseja fazer?"))
        if escolha == 1:
            valor = float(input("Valor do saque: "))
            sacar(conta_logada, valor)
        elif escolha == 2:
            valor = float(input("Valor do depósito: "))
            depositar(conta_logada, valor)
        elif escolha == 3:
            destino_nome = input("Nome da conta destino: ")
            destino_senha = input("Senha da conta destino: ")
            codigo_destino = hash(destino_nome+destino_senha)
            valor = float(input("Valor da transferência: "))
            transferir(conta_logada, codigo_destino, valor)
        elif escolha == 4:
            listar_saldo(conta_logada)
        elif escolha == 5:
            conta_logada = 0