import unittest

from svmlight import Model


class ModelTestCase(unittest.TestCase):
    def test_construction_creates_invalid_model(self):
        m = Model()
        self.assertRaises(ValueError, m.__getattribute__, 'bias')


if __name__ == '__main__':
    unittest.main()
