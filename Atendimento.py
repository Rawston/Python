"""
Crie um programa que controlará a fila de atendimento em uma receção. O usuário deverá escolher entre:

*Consultar a fila atual: Mostrar quem está na fila no momento, por ordem de chegada.
*Incluir alguém na fila: Coloca o nome e RG de um cliente na fila.
*Atender ao próximo cliente: Quando selecionada esta opção, o próximo cliente da fila será retirado desta e será mostrada
a mensagem "Atendendo ao cliente 'nome do cliente' - 'RG do Cliente'. Se a fila estiver vazia, exibir "Nenhum cliente a atender".
Solução:
"""
fila = []
quantidade_cliente = 0
while True:
    opcao = ''
    print('\n' * 100) # Limpa a tela
    print('Menu do Sistema:')
    print('1. Incluir cliente na fila')
    print('2. Listar pessoa na fila')
    print('3. Atender o proximo cliente')
    print('4. Sair do programa')
    opcao = int(input('Sua escolha -> '))
    if opcao == 1:
        quantidade_cliente = quantidade_cliente + 1
        print('\n' * 100) #Limpa a tela
        nome = input('Digite o nome do cliente: ')
        rg = input('Digite o RG do cliente:')
        cliente = {
           'nome': nome,
           'rg': rg
        }
        fila.append(cliente)
    elif opcao == 2:
        if len(fila) > 0 :
            print('\n' * 100) # Limpa a tela
            for indice in range(0, len(fila)):
                print(f'{indice + 1}-{fila[indice][rg]}-{fila[indice][nome]}')
            input('Tecle <enter> para retornar ao menu...')
        else:
            print('Fila vazia !')
            input('Tecle <enter> para retornar ao menu...')
    elif opcao == 3:
        if len(fila) > 0 :
            print('\n' * 100) # Limpa a tela
            cliente = fila.pop(0)
            print(f'Atendendo o cliente: {cliente[nome]} - RG:{cliente[rg]}')
            print(f'Restam {len(fila)} clientes na fila.')
            input('Tecle <enter> para retornar ao menu...')
        else:
            print('Fila vazia !')
            input('Tecle <enter> para retornar ao menu...')
    elif opcao == 4:
        break
print('Programa finalizado pelo usuário.')

