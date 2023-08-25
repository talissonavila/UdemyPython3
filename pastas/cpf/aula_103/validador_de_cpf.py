# 657.990.470-44
# 746.824.890-70
import re

# possivel_cpf = input("Insira seu cpf[Com pontos e o traço]: ")
possivel_cpf = '111.111.111-11'
possivel_cpf_numeros = re.sub(r'[^0-9]','',possivel_cpf)

cpf = possivel_cpf_numeros[:9]

teste_de_repetidos = possivel_cpf[0] * len(possivel_cpf_numeros)

multiplicador = 10
valor_cpf = 0
for digito in cpf:
    valor_cpf += int(digito) * multiplicador
    multiplicador-=1
resultado_primeiro_digito = valor_cpf * 10
resto_do_resultado = resultado_primeiro_digito % 11
if resto_do_resultado > 9:
    primeiro_digito = 0
else:
    primeiro_digito = resto_do_resultado


cpf = cpf + str(primeiro_digito)
multiplicador = 11
valor_cpf = 0
for digito in cpf:
    valor_cpf += int(digito) * multiplicador
    multiplicador -= 1
resultado_segundo_digito = valor_cpf * 10
resto_do_resultado = resultado_segundo_digito % 11
if resto_do_resultado > 9:
    segundo_digito = 0
else:
    segundo_digito = resto_do_resultado



cpf = cpf + str(segundo_digito)
novo_cpf = ""
for count in range (len(cpf)):
    if count == 9:
        novo_cpf += "-" + cpf[count]
        continue
    if count == 3 or count == 6:
        novo_cpf += "." + cpf[count]
    else:
        novo_cpf += cpf[count]

if possivel_cpf != novo_cpf or teste_de_repetidos == possivel_cpf_numeros:
    print("CPF inválido.")
else:
    print(f"{possivel_cpf} é válido.")