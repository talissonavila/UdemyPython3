class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{key}={value}' for key, value in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'
    
    def __repr__(self):
        return self.__str__()
    

class MonoStateSimple(StringReprMixin):
    _state = {}

    def __init__(self, first_name=None, last_name=None):
        self.__dict__ = self._state

        if first_name is not None:
            self.first_name = first_name
        
        if last_name is not None:
            self.last_name = last_name
    

if __name__ == '__main__':
    monostate1 = MonoStateSimple(first_name='Jonny')
    monostate2 = MonoStateSimple(last_name='Calleri')

    print(monostate1)
    print(monostate2)