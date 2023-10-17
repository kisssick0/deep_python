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
            CrochetClothes(13, {'cotton': 50, 'acrylic': 10}, right_piece)
        with self.assertRaises(ValueError):
            CrochetClothes(0.5, {'cotton': 50, 'smth': 50}, right_piece)

        self.assertEqual(right_thing.composition, {'cotton': 50, 'acrylic': 30.5, 'wool': 19.5})

    def test_piece(self):
        right_hook = 5
        right_composition = {'cotton': 100}
        right_thing = CrochetClothes(right_hook, right_composition, 'sweater')
        self.assertEqual(right_thing.piece, 'sweater')

        with self.assertRaises(TypeError):
            CrochetClothes(right_hook, right_composition, 5)
        with self.assertRaises(ValueError):
            CrochetClothes(13, right_composition, 'smth')

        self.assertEqual(right_thing.piece, 'sweater')


if __name__ == '__main__':
    unittest.main()