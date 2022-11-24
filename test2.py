import unittest

from program import divide

class TestDiv(unittest.TestCase):
	def test_4(self):
		a_4 = 87
		b_4 = 8
		result = divide(a_1, b_1)
		self.assertEqual(result, 7)
		
	def test_2(self):
		a_5 = 340
		b_5 = 23
		result = divide(a_2, b_2)
		self.assertEqual(result, 11)
    

if __name__ == '__main__':
	unittest.main()
