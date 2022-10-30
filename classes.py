from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def _get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self, items: dict, capacity=40):
        self.__items = items
        self.__capacity = capacity

    def __str__(self):
        st = "\n"

        for key, value in self.__items.items():
            st += f"{value} {key}\n"
        return st

    def add(self, name, count):
        if name in self.__items.keys():
            if self._get_free_space() < count:
                print("Не хватает места на складе, попробуйте заказать меньше")
                return False
            else:
                self.__items[name] += count
                return True
        else:
            if self._get_free_space() < count:
                print("Не хватает места на складе, попробуйте заказать меньше")
                return False
            else:
                self.__items[name] = count
                return True

    def remove(self, name, count):
        if self.__items[name] < count:
            print("Не хватает на складе, попробуйте заказать меньше")
            return False
        else:
            self.__items[name] -= count
            return True

    def _get_free_space(self):
        current_space = 0

        for value in self.__items.values():
            current_space += value

        return self.__capacity - current_space

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items.keys())


class Shop(Store):
    def __init__(self, items: dict, capacity=20):
        super().__init__(items, capacity)
        self.capacity = capacity

    def add(self, name, count):
        if self.get_unique_items_count() >= 5 or self._get_free_space() < count:
            print("В магазине недостаточно места, попробуйте что то другое")
            return False
        else:
            super().add(name, count)
            return True


class Request:
    def __init__(self, request_str):
        req_list = request_str.split()
        self.__amount = int(req_list[1])
        self.__product = req_list[2]
        self.__from = req_list[4]
        self.__to = req_list[6]

    def move(self):
        return {
                "from": self.__from,
                "to": self.__to,
                "amount": self.__amount,
                "product": self.__product
                }
