import os
print('Bom dia trabalhador!\n')

tarefas = []

while True:
    nova_tarefa = input('Informe a nova tarefa (no final deixe vazio para encerrar e exibir a lista): ') # usuário informa as tarefas
    if nova_tarefa != '': # verifica se o usuário inseiu nova tarefa
        tarefas.append(nova_tarefa)
        continue
    else:
        break
os.system('cls')
print(f'{'-'*30} LISTA DE TAREFAS DO DIA {'-'*30}')
for tarefa in tarefas:
    print(tarefa)
print('\nObrigada, bom dia de trabalho!')