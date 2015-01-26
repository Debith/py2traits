import unittest
from pytraits.targets.clazz import ClassTarget

class TestClass:
    pass

class TestClassTarget(unittest.TestCase):
    def test_hash_matches_text_class(self):
        class_target = ClassTarget(TestClass)
        self.assertEqual(hash(class_target), hash("class"))

    def test_is_comparable(self):
        class_target_pri = ClassTarget(TestClass)
        class_target_sec = ClassTarget(TestClass)

        self.assertEqual(class_target_pri, class_target_sec)

    def test_can_be_used_as_key_in_dictionary(self):
        items = dict()
        items[hash(ClassTarget())] = 1

        class_target = ClassTarget(TestClass)
        self.assertEqual(items[class_target], 1)

if __name__ == '__main__':
    unittest.main()
