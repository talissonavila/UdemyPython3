# maria pegou 1kk pra pagar em 5 anos
# data inicio é 20/12/2020
# data de pagamento é dia 20
# criar a data final do emprestimo
# criar a data do emprestimo
# mostrar todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta



valor_emprestimo = 1_000_000
parcelas = relativedelta(months=60)
data_inicial_do_emprestimo = datetime(2020, 12, 20)
data_final_do_emprestimo = data_inicial_do_emprestimo + parcelas



data_iteradora = data_inicial_do_emprestimo

datas_das_parcelas = []
while data_iteradora < data_final_do_emprestimo:
    datas_das_parcelas.append(data_iteradora)
    data_iteradora += relativedelta(months=1)

valor_da_parcela = valor_emprestimo / len(datas_das_parcelas)
print(f'Você pegou R${valor_emprestimo:,} a serem pagos em {len(datas_das_parcelas)} parcelas.\nVeja a simulação de pagamentos com juros de 0%.\n')
count = 0 
for parcela in datas_das_parcelas:
    count += 1
    print(f'Parcela {count:0>2d}. Data da parcela {parcela.strftime("%d/%m/%Y")}. Valor R${valor_da_parcela:,.2f}\n')
