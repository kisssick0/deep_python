import unittest
from generator import gen_search_string as gss


class TestGenerator(unittest.TestCase):
    file_name = "mytext.txt"

    def test_empty_words(self):
        input_words = []
        output_str = []

        self.assertEqual(str, type(self.file_name))
        result = list(gss(self.file_name, input_words))

    def test_some_words(self):
        input_words = ["заснуть", "проснуться"]
        output_str = ["Таким образом вы сможете спокойно заснуть"
                      " и не испытывать чувства тяжести в желудке\n"]

        self.assertEqual(str, type(self.file_name))
        result = list(gss(self.file_name, input_words))
        self.assertEqual(output_str, result)

    def test_upper_case_words(self):
        input_words = ["ОДНАКО", "СНЕ", "СЧАСТЛИВЫМИ"]
        output_str = ['Однако помните что лучше принимать их с пищей которая может их растворить\n',
                      'Не забывайте о правильном Питании сне и физической активности\n',
                      'Все эти меры помогут вам быть здоровыми и счастливыми\n']

        self.assertEqual(str, type(self.file_name))
        result = list(gss(self.file_name, input_words))
        self.assertEqual(output_str, result)

        input_words = ["Пищей", "Питании", "Все"]
        output_str = ['Однако помните что лучше принимать их с пищей которая может их растворить\n',
                      'Не забывайте о правильном Питании сне и физической активности\n',
                      'Все эти меры помогут вам быть здоровыми и счастливыми\n']

        self.assertEqual(str, type(self.file_name))
        result = list(gss(self.file_name, input_words))
        self.assertEqual(output_str, result)

    def test_lower_case_words(self):
        input_words = ["помните", "питании", "все"]
        output_str = ['Однако помните что лучше принимать их с пищей которая может их растворить\n',
                      'Не забывайте о правильном Питании сне и физической активности\n',
                      'Все эти меры помогут вам быть здоровыми и счастливыми\n']

        self.assertEqual(str, type(self.file_name))
        result = list(gss(self.file_name, input_words))
        self.assertEqual(output_str, result)

    def test_part_words(self):
        input_words = ["помнит", "н", "здоровым"]
        output_str = []

        self.assertEqual(str, type(self.file_name))
        result = list(gss(self.file_name, input_words))
        self.assertEqual(output_str, result)

    def test_two_searching_words_in_one_string(self):
        input_words = ['растение', 'сегодня']
        output_str = ['Сегодня растение я хочу рассказать вам о нескольких способах которые помогут вам улучшить ваше здоровье и благополучие\n']
        self.assertEqual(str, type(self.file_name))
        result = list(gss(self.file_name, input_words))
        self.assertEqual(output_str, result)

    def test_search_full_string(self):
        input_words =  ['Много собак очень много собак бегут\n']
        output_str = ['Много собак очень много собак бегут\n']
        self.assertEqual(str, type(self.file_name))
        result = list(gss(self.file_name, input_words))
        self.assertEqual(output_str, result)


if __name__ == '__main__':
    unittest.main()
