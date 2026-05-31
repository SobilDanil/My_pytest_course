import pytest
from src.shopping_cart import ShoppingCart


# 1. Создаем фикстуру
@pytest.fixture
def filled_cart():
    """Создает и возвращает корзину с двумя товарами."""
    # 2. Здесь находится наш код ПОДГОТОВКИ (Setup)
    cart = ShoppingCart()
    cart.add_item("apple", price=10)
    cart.add_item("banana", price=20)
    # 3. Возвращаем подготовленный объект
    return cart


# 4. Пишем тест, который ЗАПРАШИВАЕТ фикстуру
def test_add_item(filled_cart):
    # `filled_cart` здесь - это тот самый объект `cart`,
    # который вернула наша фикстура
    filled_cart.add_item("cherry", price=30)
    assert "cherry" in filled_cart.items


def test_get_total_price(filled_cart):
    # Мы можем использовать ту же самую фикстуру в другом тесте!
    assert filled_cart.get_total_price() == 30

    # tests/test_file_operations.py

    # Ничего импортировать для tmp_path не нужно!


def test_file_creation_and_reading(tmp_path):
    # tmp_path - это объект pathlib.Path, указывающий на временную папку
    # Например: /tmp/pytest-of-user/pytest-0/test_file_creation_and_reading0
    print(f"Временная папка: {tmp_path}")

    # Создаем поддиректорию внутри временной папки
    data_dir = tmp_path / "data"  # Удобный синтаксис pathlib для соединения путей
    data_dir.mkdir()

    # Создаем путь к нашему файлу
    file_path = data_dir / "my_file.txt"

    # Записываем в файл текст с помощью удобного метода
    file_path.write_text("Hello from tmp_path!")

    # Проверяем, что файл существует и содержит правильный текст
    assert file_path.exists()
    assert file_path.read_text() == "Hello from tmp_path!"

# Вам не нужно писать НИКАКОГО кода для очистки. Pytest сделает все за вас.


