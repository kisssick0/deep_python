import unittest
from descriptor import CrochetClothes


class TestDescriptor(unittest.TestCase):
    def test_hook(self):
        right_composition = {'cotton': 100}
        right_piece = 'sweater'
        right_thing = CrochetClothes(5.5, right_composition, right_piece)
        self.assertEqual(right_thing.hook, 5.5)

        with self.assertRaises(TypeError):
            CrochetClothes('aa', right_composition, right_piece)
        with self.assertRaises(ValueError):
            CrochetClothes(13, right_composition, right_piece)
        with self.assertRaises(ValueError):
            CrochetClothes(0.5, right_composition, right_piece)
        with self.assertRaises(ValueError):
            CrochetClothes(8.3, right_composition, right_piece)

        self.assertEqual(right_thing.hook, 5.5)

    def test_composition(self):
        right_hook = 5
        right_piece = 'sweater'
        right_thing = CrochetClothes(right_hook, {'cotton': 50, 'acrylic': 30.5, 'wool': 19.5}, right_piece)
        self.assertEqual(right_thing.composition, {'cotton': 50, 'acrylic': 30.5, 'wool': 19.5})

        with self.assertRaises(TypeError):
            CrochetClothes(right_hook, 'aaaaa', right_piece)
        with self.assertRaises(ValueError):
            CrochetClothes(right_hook, {'cotton': 50, 'acrylic': 10}, right_piece)
        with self.assertRaises(ValueError):
            CrochetClothes(right_hook, {'cotton': 50, 'smth': 50}, right_piece)

        self.assertEqual(right_thing.composition, {'cotton': 50, 'acrylic': 30.5, 'wool': 19.5})

    def test_piece(self):
        right_hook = 5
        right_composition = {'cotton': 100}
        right_thing = CrochetClothes(right_hook, right_composition, 'sweater')
        self.assertEqual(right_thing.piece, 'sweater')

        with self.assertRaises(TypeError):
            CrochetClothes(right_hook, right_composition, 5)
        with self.assertRaises(ValueError):
            CrochetClothes(right_hook, right_composition, 'smth')

        self.assertEqual(right_thing.piece, 'sweater')

    def test_two_class_objects(self):
        inst1 = CrochetClothes(5, {'cotton': 100}, 'sweater')
        inst2 = CrochetClothes(10, {'linen': 100}, 'bag')

        self.assertEqual(inst1.hook, 5)
        self.assertEqual(inst2.hook, 10)
        self.assertEqual(inst1.composition, {'cotton': 100})
        self.assertEqual(inst2.composition, {'linen': 100})
        self.assertEqual(inst1.piece, 'sweater')
        self.assertEqual(inst2.piece, 'bag')

        inst1.hook = 6
        self.assertEqual(inst1.hook, 6)
        self.assertEqual(inst2.hook, 10)
        inst2.hook = 11
        self.assertEqual(inst1.hook, 6)
        self.assertEqual(inst2.hook, 11)

        inst1.composition = {'cotton': 50, 'acrylic': 50}
        self.assertEqual(inst1.composition, {'cotton': 50, 'acrylic': 50})
        self.assertEqual(inst2.composition, {'linen': 100})
        inst2.composition = {'acrylic': 100}
        self.assertEqual(inst1.composition, {'cotton': 50, 'acrylic': 50})
        self.assertEqual(inst2.composition, {'acrylic': 100})

        inst1.piece = 'vest'
        self.assertEqual(inst1.piece, 'vest')
        self.assertEqual(inst2.piece, 'bag')
        inst2.piece = 'top'
        self.assertEqual(inst1.piece, 'vest')
        self.assertEqual(inst2.piece, 'top')

    def test_wrong_to_vallid_values(self):
        inst = CrochetClothes(6, {'cotton': 100}, 'sweater')
        with self.assertRaises(ValueError):
            inst.hook = 0
        inst.hook = 5
        self.assertEqual(inst.hook, 5)

        with self.assertRaises(ValueError):
            inst.composition = {'smth': 100}
        inst.composition = {'linen': 100}
        self.assertEqual(inst.composition, {'linen': 100})

        with self.assertRaises(ValueError):
            inst.piece = 'aaaa'
        inst.piece = 'vest'
        self.assertEqual(inst.piece, 'vest')


if __name__ == '__main__':
    unittest.main()
