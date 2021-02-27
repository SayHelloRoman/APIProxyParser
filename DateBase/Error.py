class Error(Exception):
    """Хз как сделать, но я сделал"""
    def __init__(self, message):
        self.message = message


class FileExtensionError(Exception):
    """Ошибка разширения файла """
    def __init__(self, message):
        self.message = message


class IdIsInTheDatabase(Exception):
    """Ошибка при создании объекта в базе данных
    объект под таким  уже есть"""
    def __init__(self, message):
        self.message = message
