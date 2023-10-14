class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
    

class AppSettings(metaclass=Singleton):
    def __init__(self) -> None:
        self.theme = 'Dark theme'
        self.font = '18px'


if __name__ == '__main__':
    app_settings1 = AppSettings()
    app_settings1.theme = 'Light theme'

    app_settings2 = AppSettings()
    print(app_settings1.theme, app_settings2.theme)
