import unittest
from homework import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rec = Rectangle(3, 8)
        self.rec1 = Rectangle(4, 4)

    def test_get_rectangle_perimeter(self):
        func_result = self.rec.get_rectangle_perimeter()
        func_result1 = self.rec1.get_rectangle_perimeter()
        self.assertEqual(func_result, 22)
        self.assertEqual(func_result1, 16)

    def test_get_rectangle_square(self):
        func_result = self.rec.get_rectangle_square()
        func_result1 = self.rec1.get_rectangle_square()
        self.assertEqual(func_result, 24)
        self.assertEqual(func_result1, 16)

    def test_get_sum_of_corners(self):
        func_result = self.rec.get_sum_of_corners(2)
        self.assertEqual(func_result, 180)

    def test_get_sum_of_corners_value_error(self):
        self.assertRaises(ValueError, self.rec.get_sum_of_corners, 5)

    def test_get_rectangle_diagonal(self):
        func_result = self.rec.get_rectangle_diagonal()
        func_result1 = self.rec1.get_rectangle_diagonal()
        self.assertAlmostEqual(func_result, 8.54400374531753)
        self.assertAlmostEqual(func_result1, 5.656854249492381)

    def test_get_radius_of_circumscribed_circle(self):
        func_result = self.rec.get_radius_of_circumscribed_circle()
        func_result1 = self.rec1.get_radius_of_circumscribed_circle()
        self.assertAlmostEqual(func_result, 8.54400374531753/2)
        self.assertAlmostEqual(func_result1, 5.656854249492381/2)


    def test_get_radius_of_inscribed_circle_error(self):
        self.assertRaises(ValueError, self.rec.get_radius_of_inscribed_circle)

    def test_get_radius_of_inscribed_circle(self):
        func_result = self.rec1.get_radius_of_inscribed_circle()
        self.assertEqual(func_result, 2)


if __name__ == '__main__':
    unittest.main()