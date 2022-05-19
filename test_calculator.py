import unittest
from calculator import MemoryCalculator

class TestMemoryCalculator(unittest.TestCase):

  def test_sum_is_zero_on_initialization(self):
    calculator = MemoryCalculator()
    self.assertEqual(0, calculator.sum())

  def test_sum_one_number(self):
    calculator = MemoryCalculator()
    calculator.add(1)
    self.assertEqual(1, calculator.sum())
    pass

  def test_sum_two_numbers(self):
    calculator = MemoryCalculator()
    calculator.add(1)
    calculator.add(1)
    self.assertEqual(2, calculator.sum())
    pass

  def test_sum_is_zero_after_calling_sum(self):
    calculator = MemoryCalculator()
    calculator.add(1)
    calculator.add(1)
    calculator.sum()
    self.assertEqual(0, calculator.sum())
    pass

  def test_sum_numbers_and_save_last_sum(self):
    calculator = MemoryCalculator(True)
    calculator.add(1)
    calculator.sum()
    calculator.add(1)
    #nao funciona está bugado
    self.assertEqual(2, calculator.sum())
    pass