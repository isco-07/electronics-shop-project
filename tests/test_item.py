"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.instantiate_csv_error import InstantiateCSVError
from src.item import Item
from src.phone import Phone


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000.0


def test_name(item):
    assert item.name == "Смартфон"


def test_name_setter(item):
    item.name = "СуперСмартфон"
    assert item.name == "СуперСмарт"


def test_instantiate_from_csv():
    Item.instantiate_from_csv("src/items.csv")
    assert len(Item.all) == 5
    with pytest.raises(FileNotFoundError, match="Отсутствует файл item.csv"):
        Item.instantiate_from_csv("item.csv")
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("tests/test_items.csv")


def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.5") == 5


def test_repr(item):
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_str(item):
    assert str(item) == "Смартфон"


def test_add(item):
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert phone.quantity + item.quantity == 25
