# Salvando de JSON para Objeto
import json


class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    @classmethod
    def from_json(cls):
        file = json.load(open('data.json'))
        return cls(**file)


pessoa_1 = Pessoa.from_json()
print(vars(pessoa_1))
