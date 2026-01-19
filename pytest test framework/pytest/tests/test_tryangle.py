from tryangle import triangle_type
import pytest

class TestTriangle:

    def test_equilateral(self):
        assert triangle_type(3, 3, 3) == 'Equilateral'

    def test_not_a_triangle(self):
        assert triangle_type(1, 2, 3) == 'Not a triangle'

    # Escreva uma suite de testes que alcance 100% de cobertura de instruções (statements) e 100% de cobertura de decisões (branches) para o código em anexo (triangle.py).
    @pytest.mark.parametrize("a, b, c, expected", [
        (3, 3, 2, 'Isosceles'),
        (4, 4, 3, 'Isosceles'),
        (5, 5, 8, 'Isosceles'),
        (3, 4, 5, 'Scalene'),
        (2, 2, 2, 'Equilateral'),
        (1, 10, 12, 'Not a triangle'),
    ])
    def test_triangle_types(self, a, b, c, expected):
        assert triangle_type(a, b, c) == expected
