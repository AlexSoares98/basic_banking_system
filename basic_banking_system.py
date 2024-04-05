import time 

saldo = 0
limite = 500
extrato = "" 
numero_saques = 0
LIMITE_SAQUES = 3

while True: 

    print("\n------- MENU PRINCIPAL -------\n")
    print("(1) Depósito")
    print("(2) Saque") 
    print("(3) Extrato") 
    print("(0) Sair")

    opcao = int(input("\nDigite a operação desejada: "))
    opcao_menu = "" 

    if opcao == 1: 
        valor = float(input("\nInsira o valor de depósito: ")) 
        if valor > 0: 
            saldo += valor 
            time.sleep(0.5)
            print(f"\nDepósito no valor de R${valor:.2f} realizado com sucesso!")
        else: 
            print("\nErro na operação! O valor informado é inválido.")
            time.sleep(0.5)

    elif opcao == 2: 
        if numero_saques >= LIMITE_SAQUES: 
            print("\nErro na operação! Número máximo de saques diário excedido.")
            time.sleep(0.5)
            continue 

        valor = float(input("\nDigite o valor de saque: ")) 
          
        if valor <= 0: 
            print("\nErro na operação! O valor informado é inválido.")
            time.sleep(0.5)
        elif valor > saldo: 
            print("\nErro na operação! Você não tem saldo suficiente.")
            time.sleep(0.5) 
            continue 
        elif valor > limite: 
            print("\nErro na operação! O valor do saque excede o limite (R$500,00).")
            time.sleep(0.5)   
        else:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1 
            time.sleep(0.5)
            print(f"\nSaque no valor de R${valor:.2f} realizado com sucesso!\n")
            print(f"Número de saques diário: {numero_saques}/3") 
            time.sleep(0.5)
    
    elif opcao == 3:
        time.sleep(0.5)
        print("\n================ EXTRATO ================\n") 
        print("Não foram realizadas movimentações." if not extrato else extrato) 
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================") 
        
    elif opcao == 0:  
        time.sleep(0.5) 
        break
    else: 
        print("\nVocê digitou uma opção inválida, digite novamente!\n")
        time.sleep(0.5) 
        continue 
           

print("\nEcerrando o sistema...\n")
time.sleep(0.5)
print("Obrigado por ser nosso cliente, volte sempre!\n") 