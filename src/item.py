import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all: list = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"
        )

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls, file_path: str) -> None:
        Item.all = []
        new_file_path = os.path.join(os.path.dirname(__file__), "..", file_path)
        with open(new_file_path) as f:
            for obj in list(csv.DictReader(f)):
                name, price, quantity = obj.values()
                cls(name, float(price), int(quantity))

    @staticmethod
    def string_to_number(string_num: str) -> int:
        float_num = float(string_num)
        return int(float_num)
