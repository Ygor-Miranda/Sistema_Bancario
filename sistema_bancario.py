#SISTEMA BANCÁRIO COM SAQUE(max 3 saques diários, valor max por saque R$ 500), DEPOSITO, EXTRATO.

menu = ('''
========= MENU =========
    [1] SAQUE
    [2] DEPÓSITO
    [3] EXTRATO
    [0] SAIR
========================\n---> ''')  # MENU DE OPÇÕES DO SISTEMA

saldo = 1000
saque = 0
deposito = 0
extrato = ''
limite_saque_diario = 0
valor_limite_de_saque = 500

while True:
    opcao = input(menu) # PRINT MENU E ESCOLHA DA OPERAÇÃO

    if int(opcao) == 1:  # SAQUE

        saque = float(input('INFORME O VALOR PARA SAQUE -> R$ ')) 

        if (saque <= saldo) and (saque <= valor_limite_de_saque) and (limite_saque_diario < 3) and (saque > 0):  # TUDO CERTO PARA SAQUE
            saldo -= saque
            limite_saque_diario += 1
            print(f'\nSAQUE DE R$ {saque} EFETUADO COM SUCESSO !!')
            extrato += f'SAQUE -> R$ -{saque:.2f}\n'

        elif (saque < 0):  # VALOR NEGATIVO PARA SAQUE
            print('*FALHA* VALOR INVÁLIDO PARA SAQUE !!')

        elif (saque <= saldo) and (saque > valor_limite_de_saque):  # VALOR DE SAQUE MAIOR QUE R$ 500,00
            print('\n*FALHA* O VALOR LIMITE PARA SAQUE É DE R$ 500,00 POR OPERAÇÃO!!')  

        elif (limite_saque_diario >= 3):  # SAQUES DIÁRIOS EXCEDIDOS
            print('\n*FALHA* EXCEDEU O LIMITE DE SAQUES DIÁRIOS !!')

        elif (saque > saldo):  # SALTO INSUFICIENTE PARA SACAR
            print('\n*FALHA* SEU SALDO É INSUFICIENTE !!')

    elif int(opcao) == 2:  # DEPÓSITO

        deposito = float(input('INFORME O VALOR DE DEPÓSITO -> R$ '))

        if deposito > 0: # TUDO CERTO PARA DEPÓSITO
            saldo += deposito
            print(f'\nDEPÓSITO DE R$ {deposito} EFETUDADO COM SUCESSO !!')
            extrato += f'DEPÓSITO -> R$ +{deposito:.2f}\n'
        else:  # VALOR NEGATIVO PARA DEPÓSITO
            print('\n*FALHA* VALOR INVÁLIDO PARA DEPÓSITO !!')
    elif int(opcao) == 3:  # EXTRATO MAIS SALDO ATUAL DA CONTA
        print('=========EXTRATO========')
        print(extrato)
        print('========================')
        print(f'SALDO ATUAL -> R$ {saldo}')
        print('========================')
    elif int(opcao) == 0:  # SAINDO DO MENU E ENCERRANDO A OPERAÇÃO
        print('FIM DA OPERAÇÃO - TENHA UM ÓTIMO DIA !!\n')
        break
    else:  # ITEM INFORMADO INCORRETO NO MENU
        print('*FALHA* OPÇÃO INVÁLIDA !!')
        continue
    

























