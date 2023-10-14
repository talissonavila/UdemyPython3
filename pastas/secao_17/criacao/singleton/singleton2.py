def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]

    return get_class


@singleton
class AppSettings:
    def __init__(self):
        self.theme = "Dark theme"
        self.font = '18px'

@singleton
class TestingSingleton:
    def __init__(self):
        pass


if __name__ == '__main__':
    app_settings1 = AppSettings()
    app_settings1.theme = 'Light theme'
    print(app_settings1.theme)

    app_settings2 = AppSettings()
    print(app_settings1.theme)

    test1 = TestingSingleton()
    test2 = TestingSingleton()
    print(test1 == test2)
    