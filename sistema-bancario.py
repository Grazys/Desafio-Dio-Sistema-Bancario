
menu = """\n
======== MENU =========
    [s] Saque
    [d] Deposito
    [e] Extrato
    [c] Sair/Cancelar
    Informe a letra da requisição que deseja realizar.
    => """

saldo = 0
LIMITE_SAQUES = 3
saques_realizados = 0
limite_valor_saque = 500
extrato = ""


while True:
    opcao = input(menu).lower()

    if opcao == "d": #DEPOSITO
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += input(f"Valor disponivel em conta é de R${saldo:.2f}\n")   
        else:
            print("Operação falhou. O valor informado é inválido")
            
    
    elif opcao == "s": # SAQUE
        valor = float(input("Informe o valor que deseja sacar: "))
        
        excedeu_limite = valor > limite_valor_saque
        excedeu_saques = saques_realizados >= LIMITE_SAQUES
        excedeu_saldo = valor > saldo

        if valor <= 0:
            print("Operação falhou! O valor informado é inválido")
        elif excedeu_limite:
            print("O valor do saque excede o valor limite diário")
        elif excedeu_saques:
            print("Você excedeu o limite diário de 3 saques")
        elif excedeu_saldo:
            print("Não há saldo suficiente na conta.")
        else:
            saldo -= valor
            extrato += f"Saque realizado no valor de R${valor:.2f}\n"
            saques_realizados += 1

    if opcao == "e": #EXTRATO
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")  
    
    elif opcao == "c": #SAIR / CANCELAR
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
