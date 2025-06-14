'''
Desafio 1: Menu Bancário
Regras:

- Deposito
    Valores positivos a conta
    * Limite de 5000,00
    Depositos aramazenados para extrato
    
- Saque
    Limite de 3 saques dia
    * Cheque Especial
    Maximo 500,00
    Informe o usuario se o saldo nao for suficiente
    Saques armazenados 
    
- Extrato
    Listar todos os saques e depositos
    * Hora nos saques e depositos
    Exibir saldo da conta
    Se for null exiba a mensagem "Não foram realizadas movimentações"
    
Exibir os valores formatados com duas casas decimais e símbolo R$.
'''

'''
Desafio 2: Menu Bancário
Regras:

10 transações diárias para uma conta
    Após atingir o limite, deve ser informado ao usuario
Data e Hora no extrato

Transformar em funções: 
    Saque: Keyword Only
        Argumentos (saldo, valor, extrato, limite, numero_saques, limite_saques)
        Retorno (saldo, extrato)
    Deposito: Postional Only
        Argumentos (saldo, valor, extrato)
        Retorno (saldo, extrato)
    Extrato: keyword and Positional
        Argumento Positional (saldo) / Argumento Keyword (extrato)
    
Criar as funções: 
    Cadastrar Usuário:
        Lista UserInfo = [ Nome, CPF, Data de Nascimento, Endereço = "logadouro, nro - bairro - cidade/sigla estado"]
        Armazenar somente o CPF
        Não permitir CPF duplicado
    Cadastrar Conta Bancária
        Lista UserAccount = [CPF, Agencia, Conta]
        Numero da Conta é Sequencial
        Agência é fixa: "0001"
        Usuário pode ter mais de uma conta
        Uma conta pertence a um único usuário
        


Addons:
    Função Listar Contas
    Função Inativar Usuário
'''

from datetime import datetime
import textwrap

menu = '''

    🏦 MENU BANCÁRIO  

        [d] Depositar  
        [s] Sacar  
        [e] Extrato  
        [cu] Cadastrar Usuário  
        [cc] Cadastrar Conta  
        [lc] Listar Contas  
        [q] Sair

=> '''


# Constantes
AGENCIA = "0001"
LIMITE_DEPOSITO = 5000
LIMITE_SAQUE = 500
LIMITE_SAQUES = 3
LIMITE_TRANSACOES = 10

# Banco de Dados

usuarios = []
contas = []


def menu():
    menu = '''
        🏦 MENU BANCÁRIO  

            [d] Depositar  
            [s] Sacar  
            [e] Extrato  
            [cu] Cadastrar Usuário  
            [cc] Cadastrar Conta  
            [lc] Listar Contas  
            [q] Sair

        => '''
    return input(textwrap.dedent(menu))

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    return saldo, extrato
def depositar(saldo, valor, extrato, /):
    return saldo, extrato
def extrato(saldo, /, *, extrato):
    return 0
def cadastrar_usuario():
    return 0
def cadastrar_conta():
    return 0
def listar_contas():
    return 0
def inativar_usuario():
    return 0


def main():
    while True:
    
        opcao = input(menu())
        
        if opcao == 'd':
            print("\n================ DEPÓSITO ================\n")
            
            valor = float(input("Informe o valor do depósito: "))
            
            print("------------------------------------------")
            
            exedeu_limite = valor > LIMITE_DEPOSITO
            
            if exedeu_limite:
                print("Operação falhou! O valor do despósito excede o limite de {LIMITE_DEPOSITO:.2f}!".format(LIMITE_DEPOSITO = LIMITE_DEPOSITO))

            elif valor > 0:
                saldo += valor
                agora = datetime.now().strftime("%H:%M:%S")
                extrato += f"\n{agora} - Depósito: R$ {valor:.2f}"
                
                print("Valor depositado: {valor:.2f}".format(valor = valor))
                print("\n==========================================")
            
            else:
                print("Operação falhou! O valor informado é inválido.")
                print("\n==========================================")
                continue
            
        elif opcao == 's':
            print("\n================= SAQUE ==================\n")
            
            valor = float(input("Informe o valor do saque: "))
            
            print("------------------------------------------")
            
            exedeu_saldo = valor > saldo
            
            exedeu_cheque_especial = (saldo - valor) < cheque_especial
            
            exedeu_limite = valor > LIMITE_SAQUE
            
            exedeu_saques = numero_saques >= LIMITE_SAQUES
            
            if exedeu_limite:
                print('Operação falhou! O valor do saque excede o limite de {LIMITE_SAQUE:.2f}!'.format(LIMITE_SAQUE = LIMITE_SAQUE))
                print("\n==========================================")
                
            elif exedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
                print("\n==========================================")
                
            elif valor > 0:
                if exedeu_saldo:
                    print("Você não tem saldo suficiente.\nGostaria de entrar no cheque especial?")
                    entrou_cheque_especial = input(menu_sim_nao)
                        
                    if entrou_cheque_especial == 's':
                        if exedeu_cheque_especial:
                            print("\n==========================================")
                            print('\nOperação falhou! O valor do saque excede o limite do cheque especial de {cheque_especial:.2f}'.format(cheque_especial = cheque_especial))
                            print("\n==========================================")
                        else:
                            saldo -= valor
                            agora = datetime.now().strftime("%H:%M:%S")
                            extrato += f'\n{agora} - Saque:    R$ {valor:.2f}'
                            numero_saques += 1
                            print("\n==========================================")
                            print("\nVocê entrou no cheque especial!")
                            print("------------------------------------------")
                            print("Valor sacado: {valor:.2f}".format(valor = valor))
                            print("\n==========================================")
                    else:
                        print("\n==========================================")
                        print("\nOperação falhou! O valor do saque excede o saldo")
                        print("\n==========================================")
                
                else:
                    saldo -= valor
                    agora = datetime.now().strftime("%H:%M:%S")
                    extrato += f'\n{agora} - Saque:    R$ {valor:.2f}'
                    numero_saques += 1
                    print("Valor sacado: {valor:.2f}".format(valor = valor))
                    print("\n==========================================")
                
            else:
                print("Operação falhou! O valor informado é inválido.")
            
        elif opcao == "e":
            agora = datetime.now().strftime("%H:%M:%S")
            print("\n================ EXTRATO =================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print("------------------------------------------")
            print(f"{agora} - SALDO:    R$ {saldo:.2f}\n")
            print("==========================================")
        
        elif opcao == "q":
            print("Você Saiu!")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            continue
        
main()
