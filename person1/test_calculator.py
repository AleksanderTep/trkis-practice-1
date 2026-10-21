import unittest
from calculator import plus, minus, proizwedenie, delenie

class TestCalculator(unittest.TestCase):
    # 1. Проверка сложения 2 штуки
    def test_plus(self):
        self.assertEqual(plus(2, 2), 4)
        self.assertEqual(plus(-1, 1), 0)

    # 2. Проверка вычитания 2 штуки
    def test_minus(self):
        self.assertEqual(minus(5, 3), 2)
        self.assertEqual(minus(3, 5), -2)

    # 3. Проверка умножения 2 штуки
    def test_proizwedenie(self):
        self.assertEqual(proizwedenie(4, 3), 12)
        self.assertEqual(proizwedenie(-2, 3), -6)

    # 4. Проверка деления 2 штуки
    def test_delenie(self):
        self.assertEqual(delenie(10, 2), 5.0)
        self.assertEqual(delenie(5, 2), 2.5)

    # 5. Проверка деления на ноль
    def test_delenie_zero(self):
        self.assertEqual(delenie(10, 0), "ошибка, я не уметь делить на нуль")

if __name__ == '__main__':
    unittest.main()
