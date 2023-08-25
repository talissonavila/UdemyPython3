from math import radians
import random
string = ''
for count in range(9):
    aleatorio = random.randint(0, 9)
    string += str(aleatorio)
print(string)