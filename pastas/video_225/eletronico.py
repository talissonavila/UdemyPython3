from log import LogFileMixin


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._eletronico_ligado = False

    def ligar(self):
        if not self._eletronico_ligado:
            self._eletronico_ligado = True

    def desligar(self):
        if self._eletronico_ligado:
            self._eletronico_ligado = False


class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar()

        if self._eletronico_ligado:
            msg = f'{self._nome} esta ligado.'
            self.log_sucess(msg)

    def desligar(self):
        super().desligar()

        if not self._eletronico_ligado:
            msg = f'{self._nome} esta desligado.'
            self.log_error(msg)
