import unittest

from svmlight import SupportVector


class SupportVectorTestCase(unittest.TestCase):
    def test_construction(self):
        self.assertEqual(str(SupportVector([(1, 1.), (2, 2.), (3, 3.)])),
                         'SupportVector({1: 1.0, 2: 2.0, 3: 3.0})')

    def test_no_zeros_allowed(self):
        self.assertRaises(ValueError, SupportVector, [(0, 1.), (1, 1.), (2, 2.)])

    def test_input_is_ordered(self):
        l = [(3, 1.0), (1, 1.0), (2, 2.0)]
        self.assertEqual(str(SupportVector(l)), 'SupportVector({})'.format(dict(sorted(l)).__repr__()))

    def test_empty_input(self):
        self.assertEqual(str(SupportVector([])), 'SupportVector({})')

    def test_iter(self):
        l = [(1, 1.0), (2, 2.0), (5, 1.0)]
        s = SupportVector(l)
        vals = [x for x in s]
        self.assertEqual(str(vals), str(l))

    def test_none_vector(self):
        self.assertEqual(str(SupportVector(None)), 'SupportVector(None)')

    def test_none_vector_length_error(self):
        s = SupportVector(None)
        self.assertRaises(ValueError, len, s)

    def test_none_vector_list_error(self):
        s = SupportVector(None)
        self.assertRaises(ValueError, list, s)

    def test_factor(self):
        s = SupportVector([(1, 1.0)])
        s.factor = 0.5
        self.assertEqual(str(s), '0.500000*SupportVector({1: 1.0})')


if __name__ == '__main__':
    unittest.main()
