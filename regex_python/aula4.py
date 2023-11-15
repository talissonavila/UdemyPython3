import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Frase 3</p> <div></div>
'''

print(re.findall(r'<[pdiv]{1,3}>.*/[pdiv]{1,3}>', texto))
print(re.findall(r'<[pdiv]{1,3}>.*?</[pdiv]{1,3}>', texto))
print(re.findall(r'<[pdiv]{1,3}>.+?</[pdiv]{1,3}>', texto))
