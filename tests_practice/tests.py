import unittest
from unittest.mock import patch
from functions import (task_1, task_2, task_3,
                       task_4, task_5, task_6,
                       task_7, task_8, task_9,
                       task_10, task_11, task_12,
                       task_13, task_14, task_15,
                       task_16, task_17, task_18,
                       task_19, task_20)


class Tests(unittest.TestCase):

    def test_task_1(self):
        a =[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        expected_result = [1, 2, 3, 5, 8, 13]
        self.assertListEqual(task_1(a, b), expected_result)

    def test_task_2(self):
        string = 'I am a good developer. I am also a writer'
        self.assertEqual(task_2(string), 5)

    def test_task_3_True(self):
        self.assertTrue(task_3(9))

    def test_task_3_False(self):
        self.assertFalse(task_3(14))

    def test_task_4(self):
        num = 48
        num1 = 157
        self.assertEqual(task_4(num), 3)
        self.assertEqual(task_4(num1), 4)

    def test_task_5(self):
        input_list = [0, 2, 3, 4, 6, 7, 10]
        self.assertListEqual(task_5(input_list), [2, 3, 4, 6, 7, 10, 0])

    def test_task_6_True(self):
        input_list = [5, 7, 9, 11]
        self.assertTrue(task_6(input_list))

    def test_task_6_False(self):
        input_list = [5, 7, 9, 11, 18]
        self.assertFalse(task_6(input_list))

    def test_task_7(self):
        input_list = [5, 3, 4, 3, 4]
        self.assertListEqual(task_7(input_list), [5])

    def test_task_8(self):
        input_list = [1, 2, 3, 4, 6, 7, 8]
        self.assertEqual(task_8(input_list), 5)

    def test_task_9(self):
        input_list = [1, 2, 3, (1, 2), 3]
        self.assertEqual(task_9(input_list), 3)

    def test_task_10(self):
        input_string = 'Hello World and Coders'
        self.assertEqual(task_10(input_string), 'sredoC dna dlroW olleH')

    def test_task_11(self):
        input_num = 63
        self.assertEqual(task_11(input_num), '1:3')

    def test_task_12(self):
        input_string_1 = 'fun&!! time'
        input_string_2 = 'I love dogs'
        self.assertEqual(task_12(input_string_1), 'time')
        self.assertEqual(task_12(input_string_2), 'love')

    @patch('functions.input', return_value='My name is Michele')
    def test_task_13(self, mock):
        self.assertEqual(task_13(), 'Michele is name My')

    @patch('functions.input', return_value=8)
    def test_task_14(self, mock):
        self.assertListEqual(task_14(), [1, 1, 2, 3, 5, 8, 13, 21])

    def test_task_15(self):
        input_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertListEqual(task_15(input_list), [4, 16, 36, 64, 100])

    def test_task_16(self):
        input_number = 4
        self.assertEqual(task_16(input_number), 10)

    def test_task_17(self):
        input_number = 4
        self.assertEqual(task_17(input_number), 24)

    def test_task_18(self):
        input_string = 'abcd'
        self.assertEqual(task_18(input_string), 'bcdE')

    def test_task_19(self):
        input_string = 'edcba'
        self.assertEqual(task_19(input_string), 'abcde')

    def test_task_20_True(self):
        num_1, num_2 = 5, 8
        self.assertTrue(task_20(num_1, num_2))

    def test_task_20_False(self):
        num_1, num_2 = 8, 5
        self.assertFalse(task_20(num_1, num_2))

    def test_task_20_Equal(self):
        num_1, num_2 = 8, 8
        self.assertEqual(task_20(num_1, num_2), '-1')


if __name__ == "__main__":
    unittest.main()
