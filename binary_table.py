from typing import List, Set
from collections import UserList
from bisect import insort_left, bisect_left


class BinaryTable(UserList):
    def __init__(self, path) -> None:
        super().__init__()
        self.data: List[str] = self._setup(path)

    @staticmethod
    def _setup(path: str) -> List[str]:
        """Получение и сортировка
        исходного списка идентификаторов"""
        with open(path) as file:
            data: Set[str] = {line.strip() for line in file}
        res_data: List[str] = list(data)
        res_data.sort(key=lambda word: [ord(char) for char in word])
        return res_data

    def add_element(self, value: str) -> str:
        """Добавление идетификаторов
        в отсортированный список"""
        if value in self.data:
            return 'Уже есть в таблице'
        insort_left(self.data, value)
        return 'Элемент успешно добавлен'

    def search_element(self, value: str) -> str:
        """Реализация алгоритма бинарного поиска"""
        lo: int = 0
        hi: int = len(self.data) - 1
        while lo <= hi:
            mid: int = (lo + hi) // 2
            if value > self.data[mid]:
                lo = mid + 1
            elif value < self.data[mid]:
                hi = mid - 1
            else:
                return f'Найден, индекс {mid}'
        return f'Элемент {value} не найден'

    def get_index(self, value: str):
        """Возвращает индекс идентификатора
        с помощью алгоритма бинарного поиска"""
        return bisect_left(self.data, value)

    def __repr__(self):
        return f'{self.data!r}'



