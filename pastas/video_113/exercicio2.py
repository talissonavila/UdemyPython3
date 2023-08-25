def par_ou_impar(numero: int):
    if numero % 2 == 0:
        return f'O número {numero} é par.'
    elif numero % 2 == 1:
        return f'O número {numero} é ímpar'
    return 'Você deveria ter enviado um valor inteiro.'


paridade_1 = par_ou_impar(12)
paridade_2 = par_ou_impar(5)
paridade_3 = par_ou_impar(-3)
paridade_4 = par_ou_impar(-10)
paridade_5 = par_ou_impar(15.3)
print(paridade_1)
print(paridade_2)
print(paridade_3)
print(paridade_4)
print(paridade_5)