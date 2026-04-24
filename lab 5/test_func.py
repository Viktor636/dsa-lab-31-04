import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides


class TestTriangleFunc(unittest.TestCase):
    
    def test_equilateral(self):
        # равносторонний
        result = get_triangle_type(5, 5, 5)
        self.assertEqual(result, "equilateral")
    
    def test_isosceles_1(self):
        # равнобедренный вариант 1
        result = get_triangle_type(5, 5, 8)
        self.assertEqual(result, "isosceles")
    
    def test_isosceles_2(self):
        # равнобедренный вариант 2
        result = get_triangle_type(8, 5, 5)
        self.assertEqual(result, "isosceles")
    
    def test_isosceles_3(self):
        # равнобедренный вариант 3
        result = get_triangle_type(5, 8, 5)
        self.assertEqual(result, "isosceles")
    
    def test_nonequilateral(self):
        # разносторонний
        result = get_triangle_type(3, 4, 5)
        self.assertEqual(result, "nonequilateral")
    
    def test_float_sides(self):
        # дробные числа
        result = get_triangle_type(1.5, 2.5, 3.0)
        self.assertEqual(result, "nonequilateral")
    
    def test_negative_side(self):
        # отрицательная сторона
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 2, 3)
    
    def test_zero_side(self):
        # нулевая сторона
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 2, 3)
    
    def test_bad_triangle_1(self):
        # 1+2=3 - не треугольник
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)
    
    def test_bad_triangle_2(self):
        # 1+2<10 - не треугольник
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 10)
    
    def test_string_side(self):
        # строка вместо числа
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type("a", 2, 3)


if __name__ == '__main__':
    unittest.main()