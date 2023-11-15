import re

texto = '''
João trouxe flores para a sua amada namorada em 10 de Janeiro de 1970.
Maria era seu nome.

Foi um ano excelente já que o brasil foi campeão mundial de futebol.
joão

Jooãoooooooo, me traz cafe.



'''

# print(re.findall(r'João|brasil', texto))

print(re.findall(r'João| br.sil', texto))

print(re.findall(r'[Jj]oão', texto))
