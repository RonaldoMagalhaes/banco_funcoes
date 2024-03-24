import textwrap
import time
import os

def menu():
    menu = """\n
    ==================  MENU ====================
    
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Conta
    [nu]\tNovo Usuario
    [q]\tSair
    
    ==============================================
    Entre com a opção desejada: """
    
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t\tR$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques
    
    if excedeu_saldo:
         print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
         time.sleep(3)
         
    elif excedeu_limite:
         print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
         time.sleep(3)
         
    elif excedeu_saques:
         print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
         time.sleep(3)

    elif valor>0:
        saldo -= valor
        extrato += f"Saque:\t\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
        time.sleep(3)
        
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        time.sleep(3)
        
    return saldo, extrato
        
        

def exibir_extrato(saldo, /,*, extrato):
    print(f"Não foram realizados movimentações.\n" if not extrato else extrato)
    print(f"Saldo:\t\t\tR$ {saldo:.2f}")  
    print("#" * 55)
    input("\n\nPressione a tecla <ENTER> para continuar...")
    
    
    
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n@@@ Já existe usuário com este CPF. @@@")
        time.sleep(2)
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa)")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado)")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("Usuário cadastrado com sucesso!")
    time.sleep(2)


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta,usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n*****  Conta criada com sucesso!  ******")
        time.sleep(3)
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrada! @@@")
    time.sleep(3)


def listar_contas(contas):
    for conta in contas:
        linha = f"""\n
            Agência: \t{conta['agencia']}
            C/C: \t\t{conta['numero_conta']}
            Titular: \t{conta['usuario']['nome']}
        """
        
        print("=" * 65)
        print(textwrap.dedent(linha))
        
    print("=" * 65)
    input("\n\nPressione a tecla <ENTER> para continuar...")
        



def main():
    
    LIMITE_SAQUE = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    
    while True:
        os.system('clear')
        opcao = menu()
        
        if opcao == "d":
            os.system('clear')
            print(" Operação Depósito ".center(55, "#"))
            print()
            valor = float(input("Informe o valor do depósito R$: "))            
            saldo, extrato = depositar(saldo,valor,extrato)
            time.sleep(3)
            
        elif opcao == "s":
            os.system('clear')
            print(" Operação de Saque ".center(55, "#"))
            print()
            valor = float(input("Informe o valor do saque R$: "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUE
            )
            
            
            
        elif opcao == "e":
            os.system('clear')
            print(" Extrato ".center(55, "#"))
            print()
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "nu":
            os.system('clear')
            print(" Cadastro de Usuários ".center(55, "#"))
            print()
            criar_usuario(usuarios)
            
        elif opcao == "nc":
            os.system('clear')
            print(" Cadastro de Contas ".center(55, "#"))
            print()
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
            
        elif opcao == "lc":
            os.system('clear')
            print(" Contas Cadastradas ".center(55, "#"))
            print()
            listar_contas(contas)
            
        elif opcao == "q":
            print("Encerrando o programa...")
            time.sleep(3)
            break
            
        


main()