

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
quantidade_de_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for indice, opcao in enumerate(opcoes):
        print(f'{indice+1}) {opcao}')
    print()
    escolha = input('Escolha uma opção: ')
    escolha_int = None
    acertou = False
    quantidade_de_opcoes = len(opcoes)
    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int > 0 and escolha_int <= quantidade_de_opcoes:
            if opcoes[escolha_int-1] == pergunta['Resposta']:
                acertou = True
                quantidade_de_acertos+= 1
    

    if acertou:
        print('Você acertou!')
    else:
        print('Você não acertou.')

if quantidade_de_acertos == 3:
    print('Parabéns. Você acertou 3 de 3 perguntas.')
else:
    print(f'Você acertou {quantidade_de_acertos} de 3 perguntas.')