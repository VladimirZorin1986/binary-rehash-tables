from collections import UserDict

# Размер хэш-таблицы
N: int = 256


def rehash(value: str, i: int) -> int:
    return (ord(value[0]) + i) % N


class RehashTable(UserDict):
    def __init__(self, path: str) -> None:
        super().__init__()
        self.data = dict.fromkeys(range(N))
        self._setup(path)

    def _setup(self, path: str) -> None:
        """Добавление начального списка идентификаторов в таблицу"""
        with open(path) as file:
            for word in file:
                self.add_element(word.strip())

    def search_element(self, value: str) -> str:
        """Поиск элемента с применением рехэширования"""
        for i in range(N):
            index = rehash(value, i)
            element = self.data.get(index)
            if not element:
                return 'Элемент не найден'
            if element == value:
                return f'Найден, позиция {index}'
        return 'Элемент не найден'

    def add_element(self, value: str) -> str:
        """Добавление элемента с применением рехэширования"""
        if None not in self.data.values():
            return 'Таблица заполнена полностью'
        if self.search_element(value) != 'Элемент не найден':
            return 'Элемент уже присутствует в таблице'
        for i in range(N):
            res_hash = rehash(value, i)
            if self.data.get(res_hash) is None:
                self.data[res_hash] = value
                return 'Элемент добавлен'

    def __repr__(self):
        return f'{self.data!r}'
















