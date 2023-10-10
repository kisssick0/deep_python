import unittest
from unittest.mock import patch
from io import StringIO

import custom_list


class TestCustomList(unittest.TestCase):
    def test_sum_two_custom_lists(self):
        cl1 = custom_list.CustomList([1, 2, 3])
        cl2 = custom_list.CustomList([4, 5])
        sum_cl1_cl2 = [5, 7, 3]

        self.assertEqual(list(cl1 + cl2), sum_cl1_cl2)
        self.assertEqual(list(cl2 + cl1), sum_cl1_cl2)

        self.assertEqual(list(cl1), list(custom_list.CustomList([1, 2, 3])))
        self.assertEqual(list(cl2), list(custom_list.CustomList([4, 5])))

        cl1 = custom_list.CustomList([4, 5])
        cl2 = custom_list.CustomList([1, 2, 3])
        sum_cl1_cl2 = [5, 7, 3]

        self.assertEqual(list(cl1 + cl2), sum_cl1_cl2)
        self.assertEqual(list(cl2 + cl1), sum_cl1_cl2)

        self.assertEqual(list(cl1), list(custom_list.CustomList([4, 5])))
        self.assertEqual(list(cl2), list(custom_list.CustomList([1, 2, 3])))

        cl1 = custom_list.CustomList([4, 5, 6])
        cl2 = custom_list.CustomList([1, 2, 3])
        sum_cl1_cl2 = [5, 7, 9]

        self.assertEqual(list(cl1 + cl2), sum_cl1_cl2)
        self.assertEqual(list(cl2 + cl1), sum_cl1_cl2)

        self.assertEqual(list(cl1), list(custom_list.CustomList([4, 5, 6])))
        self.assertEqual(list(cl2), list(custom_list.CustomList([1, 2, 3])))

    def test_sum_custom_list_and_list(self):
        clst = custom_list.CustomList([1, 2, 3])
        lst = [4, 5]
        sum_cl_lst = [5, 7, 3]

        self.assertEqual(list(clst + lst), sum_cl_lst)
        self.assertEqual(list(lst + clst), sum_cl_lst)

        self.assertEqual(list(clst), list(custom_list.CustomList([1, 2, 3])))
        self.assertEqual(lst, [4, 5])

        clst = custom_list.CustomList([4, 5])
        lst = [1, 2, 3]
        sum_cl_lst = [5, 7, 3]

        self.assertEqual(list(clst + lst), sum_cl_lst)
        self.assertEqual(list(lst + clst), sum_cl_lst)

        self.assertEqual(list(clst), list(custom_list.CustomList([4, 5])))
        self.assertEqual(lst, [1, 2, 3])

        clst = custom_list.CustomList([4, 5, 6])
        lst = [1, 2, 3]
        sum_cl_lst = [5, 7, 9]

        self.assertEqual(list(clst + lst), sum_cl_lst)
        self.assertEqual((lst + clst), sum_cl_lst)

        self.assertEqual(list(clst), list(custom_list.CustomList([4, 5, 6])))
        self.assertEqual(lst, [1, 2, 3])

    def test_sub_two_custom_lists(self):
        cl1 = custom_list.CustomList([1, 2, 3])
        cl2 = custom_list.CustomList([4, 5])
        sub_cl1_cl2 = [-3, -3, 3]
        sub_cl2_cl1 = [3, 3, -3]

        self.assertEqual(list(cl1 - cl2), sub_cl1_cl2)
        self.assertEqual(list(cl2 - cl1), sub_cl2_cl1)

        self.assertEqual(list(cl1), list(custom_list.CustomList([1, 2, 3])))
        self.assertEqual(list(cl2), list(custom_list.CustomList([4, 5])))

        cl1 = custom_list.CustomList([4, 5])
        cl2 = custom_list.CustomList([1, 2, 3])
        sub_cl1_cl2 = [3, 3, -3]
        sub_cl2_cl1 = [-3, -3, 3]

        self.assertEqual(list(cl1 - cl2), sub_cl1_cl2)
        self.assertEqual(list(cl2 - cl1), sub_cl2_cl1)

        self.assertEqual(list(cl1), list(custom_list.CustomList([4, 5])))
        self.assertEqual(list(cl2), list(custom_list.CustomList([1, 2, 3])))

        cl1 = custom_list.CustomList([4, 5, 6])
        cl2 = custom_list.CustomList([1, 2, 3])
        sub_cl1_cl2 = [3, 3, 3]
        sub_cl2_cl1 = [-3, -3, -3]

        self.assertEqual(list(cl1 - cl2), sub_cl1_cl2)
        self.assertEqual(list(cl2 - cl1), sub_cl2_cl1)

        self.assertEqual(list(cl1), list(custom_list.CustomList([4, 5, 6])))
        self.assertEqual(list(cl2), list(custom_list.CustomList([1, 2, 3])))

    def test_sub_custom_list_and_list(self):
        clst = custom_list.CustomList([1, 2, 3])
        lst = custom_list.CustomList([4, 5])
        sub_cl_lst = [-3, -3, 3]
        sub_lst_cl = [3, 3, -3]

        self.assertEqual(list(clst - lst), sub_cl_lst)
        self.assertEqual(list(lst - clst), sub_lst_cl)

        self.assertEqual(list(clst), list(custom_list.CustomList([1, 2, 3])))
        self.assertEqual(lst, [4, 5])

        clst = custom_list.CustomList([4, 5])
        lst = custom_list.CustomList([1, 2, 3])
        sub_cl_lst = [3, 3, -3]
        sub_lst_cl = [-3, -3, 3]

        self.assertEqual(list(clst - lst), sub_cl_lst)
        self.assertEqual(list(lst - clst), sub_lst_cl)

        self.assertEqual(list(clst), list(custom_list.CustomList([4, 5])))
        self.assertEqual(lst, [1, 2, 3])

        clst = custom_list.CustomList([1, 2, 3])
        lst = custom_list.CustomList([4, 5, 6])
        sub_cl_lst = [-3, -3, -3]
        sub_lst_cl = [3, 3, 3]

        self.assertEqual(list(clst - lst), sub_cl_lst)
        self.assertEqual(list(lst - clst), sub_lst_cl)

        self.assertEqual(list(clst), list(custom_list.CustomList([1, 2, 3])))
        self.assertEqual(lst, [4, 5, 6])

    def test_lt(self):
        cl1 = custom_list.CustomList([1, 2, 3])
        cl2 = custom_list.CustomList([4, 5])
        sum_cl1 = 6
        sum_cl2 = 9

        self.assertTrue(cl1 < cl2)
        self.assertEqual(cl1 < cl2, sum_cl1 < sum_cl2)
        self.assertFalse(cl2 < cl1)
        self.assertEqual(cl2 < cl1, sum_cl2 < sum_cl1)

        self.assertEqual(cl1, custom_list.CustomList([1, 2, 3]))
        self.assertEqual(cl2, custom_list.CustomList([4, 5]))

    def test_le(self):
        cl1 = custom_list.CustomList([1, 2, 3])
        cl2 = custom_list.CustomList([4, 5])
        sum_cl1 = 6
        sum_cl2 = 9

        self.assertTrue(cl1 <= cl2)
        self.assertEqual(cl1 <= cl2, sum_cl1 <= sum_cl2)
        self.assertFalse(cl2 <= cl1)
        self.assertEqual(cl2 <= cl1, sum_cl2 <= sum_cl1)

        self.assertEqual(cl1, custom_list.CustomList([1, 2, 3]))
        self.assertEqual(cl2, custom_list.CustomList([4, 5]))

        cl1 = custom_list.CustomList([1, 2, 3])
        cl2 = custom_list.CustomList([1, 0, 5])
        sum_cl1 = 6
        sum_cl2 = 6

        self.assertTrue(cl1 <= cl2)
        self.assertEqual(cl1 <= cl2, sum_cl1 <= sum_cl2)
        self.assertTrue(cl2 <= cl1)
        self.assertEqual(cl2 <= cl1, sum_cl2 <= sum_cl1)

        self.assertEqual(cl1, custom_list.CustomList([1, 2, 3]))
        self.assertEqual(cl2, custom_list.CustomList([1, 0, 5]))

    def test_eq(self):
        cl1 = custom_list.CustomList([1, 2, 3])
        cl2 = custom_list.CustomList([3, 1, 1, 1])
        cl3 = custom_list.CustomList([3, 1])
        sum_cl1 = 6
        sum_cl2 = 6
        sum_cl3 = 4

        self.assertTrue(cl1 == cl2)
        self.assertEqual(cl1 == cl2, sum_cl1 == sum_cl2)
        self.assertTrue(cl2 == cl1)
        self.assertEqual(cl2 == cl1, sum_cl2 == sum_cl1)
        self.assertFalse(cl2 == cl3)
        self.assertEqual(cl2 == cl3, sum_cl3 == sum_cl2)

        self.assertEqual(cl1, custom_list.CustomList([1, 2, 3]))
        self.assertEqual(cl2, custom_list.CustomList([3, 1, 1, 1]))
        self.assertEqual(cl3, custom_list.CustomList([3, 1]))

    def test_ne(self):
        cl1 = custom_list.CustomList([1, 2, 3])
        cl2 = custom_list.CustomList([3, 1, 1, 1])
        cl3 = custom_list.CustomList([3, 1])
        sum_cl1 = 6
        sum_cl2 = 6
        sum_cl3 = 4

        self.assertFalse(cl1 != cl2)
        self.assertEqual(cl1 != cl2, sum_cl1 != sum_cl2)
        self.assertFalse(cl2 != cl1)
        self.assertEqual(cl2 != cl1, sum_cl2 != sum_cl1)
        self.assertTrue(cl2 != cl3)
        self.assertEqual(cl2 != cl3, sum_cl3 != sum_cl2)

        self.assertEqual(cl1, custom_list.CustomList([1, 2, 3]))
        self.assertEqual(cl2, custom_list.CustomList([3, 1, 1, 1]))
        self.assertEqual(cl3, custom_list.CustomList([3, 1]))

    def test_gt(self):
        cl1 = custom_list.CustomList([4, 5])
        cl2 = custom_list.CustomList([1, 2, 3])
        sum_cl1 = 9
        sum_cl2 = 6

        self.assertTrue(cl1 > cl2)
        self.assertEqual(cl1 > cl2, sum_cl1 > sum_cl2)
        self.assertFalse(cl2 > cl1)
        self.assertEqual(cl2 > cl1, sum_cl2 > sum_cl1)

        self.assertEqual(cl1, custom_list.CustomList([4, 5]))
        self.assertEqual(cl2, custom_list.CustomList([1, 2, 3]))

    def test_ge(self):
        cl1 = custom_list.CustomList([4, 5])
        cl2 = custom_list.CustomList([1, 2, 3])
        sum_cl1 = 9
        sum_cl2 = 6

        self.assertTrue(cl1 >= cl2)
        self.assertEqual(cl1 >= cl2, sum_cl1 >= sum_cl2)
        self.assertFalse(cl2 >= cl1)
        self.assertEqual(cl2 >= cl1, sum_cl2 >= sum_cl1)

        self.assertEqual(cl1, custom_list.CustomList([4, 5]))
        self.assertEqual(cl2, custom_list.CustomList([1, 2, 3]))

        cl1 = custom_list.CustomList([1, 2, 3])
        cl2 = custom_list.CustomList([1, 0, 5])
        sum_cl1 = 6
        sum_cl2 = 6

        self.assertTrue(cl1 >= cl2)
        self.assertEqual(cl1 >= cl2, sum_cl1 >= sum_cl2)
        self.assertTrue(cl2 >= cl1)
        self.assertEqual(cl2 >= cl1, sum_cl2 >= sum_cl1)

        self.assertEqual(cl1, custom_list.CustomList([1, 2, 3]))
        self.assertEqual(cl2, custom_list.CustomList([1, 0, 5]))

    def test_print_str(self):
        clst = custom_list.CustomList([1, 2, 3])
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(clst)
            self.assertEqual(fake_out.getvalue(), "[1, 2, 3] sum=6\n")

        self.assertEqual(clst, custom_list.CustomList([1, 2, 3]))

    def test_str(self):
        clst = custom_list.CustomList([1, 2, 3])
        self.assertEqual(str(clst), "[1, 2, 3] sum=6")

        self.assertEqual(clst, custom_list.CustomList([1, 2, 3]))

    def test_empty(self):
        cl1 = custom_list.CustomList([])
        cl2 = custom_list.CustomList([])
        lst = []
        cl3 = custom_list.CustomList([])

        self.assertEqual(cl1 + cl2, cl3)
        self.assertEqual(cl2 + cl3, cl3)
        self.assertEqual(cl1 + lst, cl3)
        self.assertEqual(lst + cl1, cl3)

        self.assertEqual(cl1 - cl2, cl3)
        self.assertEqual(cl2 - cl1, cl3)
        self.assertEqual(lst - cl2, cl3)
        self.assertEqual(cl2 - lst, cl3)

        self.assertTrue(cl1 == cl2)
        self.assertFalse(cl1 != cl2)
        self.assertFalse(cl1 > cl2)
        self.assertFalse(cl1 < cl2)
        self.assertTrue(cl1 <= cl2)
        self.assertTrue(cl1 >= cl2)

        self.assertEqual(cl1, custom_list.CustomList([]))
        self.assertEqual(cl2, custom_list.CustomList([]))
        self.assertEqual(cl3, custom_list.CustomList([]))


if __name__ == '__main__':
    unittest.main()
