class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.theme = 'Dark mode'
        self.font = '18px'

if __name__ == '__main__':
    app_settings1 = AppSettings()
    app_settings1.theme = 'Light mode'
    print(app_settings1.theme)
    app_settings2 = AppSettings()


    print(app_settings2.theme)
    print(app_settings1.theme)
