import requests


class HHapi:
    """Класс работы с API hh"""

    def __init__(self):
        self.__url = "https://api.hh.ru"
        self._headers = {"User-Agent": "HH-User-Agent"}
        self._params = {"per_page": 100, "page": 0, "only_with_salary": True}
        self.employers = []