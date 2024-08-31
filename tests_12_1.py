# Файл: tests_12_1.py

import unittest
from runner import Runner  # Убедитесь, что путь к файлу runner.py указан правильно

class RunnerTest(unittest.TestCase):
    # Тест инициализации объекта Runner
    def test_initialization(self):
        runner = Runner('Test Runner')
        self.assertEqual(runner.name, 'Test Runner')  # Убеждаемся, что имя установлено корректно
        self.assertEqual(runner.distance, 0)  # Убеждаемся, что начальное расстояние равно 0

    # Тест функциональности ходьбы
    def test_walk(self):
        runner = Runner('Test Runner')
        for _ in range(10):
            runner.walk()  # Симулируем ходьбу 10 раз
        self.assertEqual(runner.distance, 50)  # Убеждаемся, что общее расстояние равно 50 (10 * 5)

    # Тест функциональности бега
    def test_run(self):
        runner = Runner('Test Runner')
        for _ in range(10):
            runner.run()  # Симулируем бег 10 раз
        self.assertEqual(runner.distance, 100)  # Убеждаемся, что общее расстояние равно 100 (10 * 10)

    # Тест смешанного движения (чередование ходьбы и бега)
    def test_mixed_movement(self):
        runner = Runner('Test Runner')
        for _ in range(5):
            runner.walk()  # Симулируем ходьбу 5 раз
            runner.run()  # Симулируем бег 5 раз
        self.assertEqual(runner.distance, 75)  # Убеждаемся, что общее расстояние равно 75 (5 * 5 + 5 * 10)

    # Тест сравнения расстояний между двумя бегунами
    def test_challenge(self):
        runner1 = Runner('Runner 1')
        runner2 = Runner('Runner 2')
        for _ in range(10):
            runner1.run()  # Бегун 1 бежит 10 раз
            runner2.walk()  # Бегун 2 ходит 10 раз
        self.assertNotEqual(runner1.distance, runner2.distance)  # Убеждаемся, что расстояния не равны
        self.assertTrue(runner1.distance > runner2.distance)  # Убеждаемся, что Бегун 1 пробежал большее расстояние

    # Тест граничного случая с нулевыми итерациями
    def test_edge_case_zero_iterations(self):
        runner = Runner('Test Runner')
        self.assertEqual(runner.distance, 0)  # Убеждаемся, что расстояние остается 0 при отсутствии движения

    # Тест граничного случая с большим количеством итераций
    def test_edge_case_large_iterations(self):
        runner = Runner('Test Runner')
        for _ in range(1000):
            runner.run()  # Симулируем бег 1000 раз
        self.assertEqual(runner.distance, 10000)  # Убеждаемся, что общее расстояние равно 10000 (1000 * 10)

if __name__ == '__main__':
    unittest.main()