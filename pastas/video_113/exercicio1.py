def multiplicador(*args):
    valor = 1
    for numero in args:
        valor *= numero
    return valor


resultado = multiplicador(2,4,6,10)
print(resultado)