import unittest

from svmlight import Learner, DocumentFactory


def get_docs():
    f = DocumentFactory()
    return [f.new(x.split()) for x in [
        'this is a nice long document',
        'this is another nice long document',
        'this is rather a short document',
        'a horrible document',
        'another horrible document']]


class LearnerTestCase(unittest.TestCase):
    def test_construction(self):
        self.assertEqual(str(Learner()),
                         'Learner(biased_hyperplane=True)')

    def test_set_biased_hyperplane(self):
        l = Learner()
        l.biased_hyperplane = False
        self.assertEqual(str(l), 'Learner(biased_hyperplane=False)')

    def test_learn(self):
        docs = get_docs()
        l = Learner()
        model = l.learn(docs, [1, 1, 1, -1, -1])
        print(model, model.bias)
        self.assertEqual(5, model.num_docs)
        self.assertEqual(10, len(model.plane))
        self.assertNotEqual(model.bias, 0)
        print(model.plane)

    def test_learn_unbiased(self):
        docs = get_docs()
        l = Learner()
        l.biased_hyperplane = False
        model = l.learn(docs, [1, 1, 1, -1, -1])
        print(model, model.bias)
        self.assertEqual(5, model.num_docs)
        self.assertEqual(10, len(model.plane))
        self.assertEqual(model.bias, 0)
        print(model.plane)

    def test_learn_classify(self):
        docs = get_docs()
        l = Learner()
        class_values = [1, 1, 1, -1, -1]
        model = l.learn(docs, class_values)
        judgments = [model.classify(d) for d in docs]
        for i in range(len(class_values)):
            binary = 1 if judgments[i] > 0 else -1
            self.assertEqual(class_values[i], binary)


if __name__ == '__main__':
    unittest.main()
