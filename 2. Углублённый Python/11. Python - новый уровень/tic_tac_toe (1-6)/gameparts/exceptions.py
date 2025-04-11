class FieldIndexError(IndexError):
    """Выбрасывается, если выбрано значение вне поля."""

    def __init__(self, 
                 message='Введённое значение за границей ирового поля!'
                ):
        super().__init__(message)


class CellOccupiedError(Exception):
    """Выбрасывается, если используется уже занятая клетка поля."""

    def __init__(self, 
                 message='Попытка изменить занятую ячейку'
                 ):
        super().__init__(message)