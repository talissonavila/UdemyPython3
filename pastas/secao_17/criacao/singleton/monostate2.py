class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{key}={value}' for key, value in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'
    
    def __repr__(self):
        return self.__str__()
    

class MonoState(StringReprMixin):
    _state = {}

    def __new__(cls, *args, **kwargs):
        _object = super().__new__(cls)
        _object.__dict__ = cls._state
        return _object

    def __init__(self, first_name=None, last_name=None):
        if first_name is not None:
            self.first_name = first_name
        
        if last_name is not None:
            self.last_name = last_name


class A(MonoState):
    pass


if __name__ == '__main__':
    monostate1 = MonoState(first_name='Jonny')
    monostate2 = A(last_name='Calleri')

    print(monostate1)
    print(monostate2)
    