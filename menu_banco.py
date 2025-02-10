'''
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

from datetime import datetime

menu = '''

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> '''

menu_sim_nao = '''

    [s] Sim
    [n] Não

=>'''

saldo = 0
cheque_especial = -500
limite_deposito = 5000
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == 'd':
        print("\n================ DEPÓSITO ================\n")
        
        valor = float(input("Informe o valor do depósito: "))
        
        print("---------------------------------------")
        
        exedeu_limite = valor > limite_deposito
        
        if exedeu_limite:
            print("Operação falhou! O valor do despósito excede o limite de {limite_deposito:.2f}!".format(limite_deposito = limite_deposito))

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
        print("\n================ SAQUE ================\n")
        
        valor = float(input("Informe o valor do saque: "))
        
        print("---------------------------------------")
        
        exedeu_saldo = valor > saldo
        
        exedeu_cheque_especial = (saldo - valor) < cheque_especial
        
        exedeu_limite = valor > limite_saque
        
        exedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if exedeu_limite:
            print('Operação falhou! O valor do saque excede o limite de {limite_saque}!'.format(limite_saque = limite_saque))
            print("\n==========================================")
            
        elif exedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            print("\n==========================================")
            
        elif valor > 0:
            if exedeu_saldo:
                print("Você não tem saldo suficiente. Gostaria de entrar no cheque especial?")
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
                        print("---------------------------------------")
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
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("---------------------------------------")
        print(f"{agora} - SALDO:    R$ {saldo:.2f}\n")
        print("==========================================")
    
    elif opcao == "q":
        print("Você Saiu!")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        continue