def listar_tarefas(lista_de_tarefas):
    print()
    if not lista_de_tarefas:
        return print('Nenhuma tarefa a listar.')

    print('TAREFAS: ')
    for tarefa in lista_de_tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(lista_de_tarefas, lista_de_tarefas_refazer):
    print()
    if not lista_de_tarefas:
        print('Nenhuma tarefa a desfazer.')
        return
    tarefa_desfeita = lista_de_tarefas.pop()
    print(f'{tarefa_desfeita} removida da lista de tarefas.')
    lista_de_tarefas_refazer.append(tarefa_desfeita)
    print()


def refazer(lista_de_tarefas, lista_de_tarefas_refazer):
    print()
    if not lista_de_tarefas_refazer:
        print('Nenhuma tarefa a refazer.')
        return
    tarefa_refeita = lista_de_tarefas_refazer.pop()
    print(f'{tarefa_refeita} adicionada na lista de tarefas.')
    lista_de_tarefas.append(tarefa_refeita)
    print()


def adicionar_tarefa(tarefa, lista_de_tarefas):
    print()
    # tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa} adicionada na lista de tarefas.')
    lista_de_tarefas.append(tarefa)


tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer ou refazer.Digite "sair" para sair do programa.')
    acao = input('Digite uma tarefa ou comando: ')
    acao = acao.lower()
    if acao == 'listar':
        listar_tarefas(tarefas)
        continue
    elif acao == "desfazer":
        desfazer(tarefas, tarefas_refazer)
        listar_tarefas(tarefas)
        continue
    elif acao == "refazer":
        refazer(tarefas, tarefas_refazer)
        listar_tarefas(tarefas)
        continue
    elif acao == 'sair':
        break
    else:
        adicionar_tarefa(acao, tarefas)
        listar_tarefas(tarefas)
        continue
