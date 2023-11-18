import re
texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Frase 3</p> <div></div>
'''

expressao_reg = r'<(?:p|div)>(.*?)<\/(?:p|div)>'

data_regex = re.findall(expressao_reg, texto)

print(data_regex)
