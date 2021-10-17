import unittest
from trail_hello import hello


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_hello(self):
        arg = "world"
        result = "hello, {}".format(arg)
        self.assertEqual(hello(arg), result)


if __name__ == '__main__':
    unittest.main()
