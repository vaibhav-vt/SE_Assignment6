import unittest

from program import divide

class TestDiv(unittest.TestCase):
	def test_4(self):
		a_4 = 87
		b_4 = 8
		result = divide(a_4, b_4)
		self.assertEqual(result, 7)
		
	def test_2(self):
		a_5 = 340
		b_5 = 23
		result = divide(a_5, b_5)
		self.assertEqual(result, 11)
    

if __name__ == '__main__':
	unittest.main()
