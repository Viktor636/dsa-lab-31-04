from triangle_func import IncorrectTriangleSides

class Triangle:
    def __init__(self, a, b, c):
        if not all(isinstance(x, (int, float)) and x > 0 for x in (a, b, c)):
            raise IncorrectTriangleSides("Стороны должны быть положительными числами")
        if a + b <= c or a + c <= b or b + c <= a:
            raise IncorrectTriangleSides("Неравенство треугольника не выполнено")
        self.a, self.b, self.c = a, b, c
    
    def triangle_type(self):
        if self.a == self.b == self.c:
            return "equilateral"
        if self.a == self.b or self.a == self.c or self.b == self.c:
            return "isosceles"
        return "nonequilateral"
    
    def perimeter(self):
        return self.a + self.b + self.c