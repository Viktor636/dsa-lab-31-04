class IncorrectTriangleSides(Exception):
    pass

def get_triangle_type(a, b, c):
    # Проверка что все числа и >0
    if not all(isinstance(x, (int, float)) and x > 0 for x in (a, b, c)):
        raise IncorrectTriangleSides("Стороны должны быть положительными")
    # Неравенство треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides("Неравенство треугольника не выполнено")
    # Тип
    if a == b == c:
        return "equilateral" # равносторонний
    if a == b or a == c or b == c: 
        return "isosceles"# равнобедренный
    return "nonequilateral" # разносторонний