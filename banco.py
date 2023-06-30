saldo = 0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUES = 3

def deposito():
    global saldo
    global extrato
    print('Você selecionou depósito.')
    valor = float(input('Digite o valor desejado: '))
    while valor <= 0:
        print('Você pode fazer depósitos a partir de R$1,00. Tente novamente.')
        valor = float(input('Digite o valor desejado: '))
    print('Depósito feito com sucesso!')    
    extrato += f'Depósito: + R$ {valor:,.2f}\n'
    saldo += valor
    print(f'Novo saldo: R$ {saldo:,.2f}')

def saque():
    global saldo
    global extrato
    global numero_saque

    print('Você selecionou SAQUE.')

    if numero_saque >= 3 or saldo <= 0:
        print('Limite de saque excedido ou saldo insuficiente. Tente novamente amanhã.')
        return

    valor = float(input('Valor do saque: '))

    while valor > saldo or valor > 500:
        if valor > saldo:
            print(f'Saldo insuficiente! Seu saldo atual: R$ {saldo:,.2f}')
        elif valor > 500:
            print('O valor do saque não pode ser maior que R$ 500. Tente novamente.')

        valor = float(input('Valor do saque: '))

    print('Saque efetuado com sucesso!')
    extrato += f'Saque: - R$ {valor:,.2f}\n'
    saldo -= valor
    numero_saque += 1
    print(f'Novo saldo: R$ {saldo:,.2f}')

continuar = True

while continuar:
    opcao = input('Seja Bem-vindo ao Banco!\n\nDigite a opção desejada:\n\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\n\n=> ').strip().lower()

    if opcao == 'd':
        deposito()
    elif opcao == 's':
        saque()
    elif opcao == 'e':
        print('\n========================= EXTRATO =========================')
        print('Não foram realizadas movimentações.' if not extrato else '\n'.join(extrato.split('\n')))
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('=========================================================== ')
    elif opcao == 'q':
        continuar = False
        print('Sessão encerrada.')
    else:
        print('Opção inválida!')

    if continuar:
        resposta = input('Deseja realizar outra operação? (s/n): ').strip().lower()
        if resposta != 's':
            continuar = False
            print('Sessão encerrada.')
