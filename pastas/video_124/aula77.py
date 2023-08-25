from time import sleep

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
print('..' * 50)
print('Bem vindo ao game quizz de python. Para ganhar você deve acertar as 3 perguntas.')
print('..' * 50)
print()
# print(perguntas[0].pop('Pergunta'))
acertos = 0
for count in range(len(perguntas)):
    print('--' * 50)
    print(f'Pergunta de número {count+1}:', end=' ')
    pergunta = perguntas[count].pop('Pergunta')
    print(pergunta)
    print('--' * 50)
    print('Opções:')
    options = perguntas[count].pop('Opções')
    correct_answer = perguntas[count].pop('Resposta')
    for count in range(4):
        sleep(1)
        print(f'{count+1}) {options[count]}')
    response = input('Sua resposta: ')
    sleep(2)
    if response == correct_answer:
        print('Certa resposta.')
        acertos+=1
    else:
        print(f'Resposta Errada.\nA resposta certa era {correct_answer}.')
if acertos == 3:
    print('Parabéns. Você ganhou!')
else:
    print(f'Não foi dessa fez. Você acertou {acertos} de 3 perguntas.')