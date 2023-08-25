from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o méotodo log.')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        mensagem_formatada = f'{msg} ({self.__class__.__name__})'
        print(f'Salvando no log: {mensagem_formatada}')
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(mensagem_formatada)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    log_print = LogPrintMixin()
    log_print.log_error('qualquer coisa')
    log_print.log_sucess('Funcionou')

    log_file = LogFileMixin()
    log_file.log_error('nao funcionou')
    log_file.log_sucess('agora funcionou')
