import unittest

from program import divide

class TestSum(unittest.TestCase):
	def test_1(self):
		a_1 = 30
		b_1 = 10
		result = divide(a_1, b_1)
		self.assertEqual(result, 3)
		
	def test_2(self):
		a_2 = 10
		b_2 = 5
		result = divide(a_2, b_2)
		self.assertEqual(result, 2)

	def test_3(self):
		a_3 = 66
		b_3 = 6
		result = divide(a_3, b_3)
		self.assertEqual(result, 11)


if __name__ == '__main__':
	unittest.main()
