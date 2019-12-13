import unittest
from immediate_greatest import my_func

class TestSample(unittest.TestCase):

    def test_myfunc1(self):
        result1 = my_func(12345967)
        self.assertEqual(result1, 12345976)

    def test_myfunc1(self):
        result1 = my_func(54321)
        self.assertEqual(result1, 54321)

    def test_myfunc1(self):
        result1 = my_func(78910231)
        self.assertEqual(result1, 78910312)

if __name__ == "__main__":
    unittest.main()
