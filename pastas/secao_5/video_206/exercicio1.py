# Salvando de Objeto para JSON
import json


class Pessoa:

    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
        return f'{self.nome} está fazendo aniversário. Agora tem {self.idade} anos.'


# class PersonEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, Pessoa):
#             return {'nome': o.nome, 'idade': o.idade}
#         return super().default(o)


pessoa_1 = Pessoa(nome='joao', idade=20)
# print(pessoa_1.fazer_aniversario())
# pessoa_json = json.dumps(pessoa_1, cls=PersonEncoder, indent=0)
# print(pessoa_json)
dict_pessoa = vars(pessoa_1)
output_file = open('data.json', 'w')
json.dump(dict_pessoa, output_file, indent=0)
output_file.close()
