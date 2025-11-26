import unittest
from testing_fundamentals01 import square

class TestSquare(unittest.TestCase):
    def test_square_of_two(self):
        result = square(2)
        self.assertEqual(result, 4)
    def test_square_of_four(self):
        result = square(4)
        self.assertEqual(result, 16)
    
if __name__ == "__main__":
  unittest.main()