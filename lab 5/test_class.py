import pytest
from triangle_class import Triangle, IncorrectTriangleSides


# тесты на тип треугольника
def test_type_equilateral():
    t = Triangle(5, 5, 5)
    assert t.triangle_type() == "equilateral"

def test_type_isosceles():
    t = Triangle(5, 5, 8)
    assert t.triangle_type() == "isosceles"

def test_type_nonequilateral():
    t = Triangle(3, 4, 5)
    assert t.triangle_type() == "nonequilateral"


# тесты на периметр
def test_perimeter_1():
    t = Triangle(5, 5, 5)
    assert t.perimeter() == 15

def test_perimeter_2():
    t = Triangle(5, 5, 8)
    assert t.perimeter() == 18

def test_perimeter_3():
    t = Triangle(3, 4, 5)
    assert t.perimeter() == 12


# тесты на ошибки
def test_error_negative():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 2, 3)

def test_error_zero():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 2, 3)

def test_error_not_triangle():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 3)

def test_error_string():
    with pytest.raises(IncorrectTriangleSides):
        Triangle("a", 2, 3)