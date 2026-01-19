from tryangle import triangle_type
#from mut1 import triangle_type
#from mut2 import triangle_type
#from mut3 import triangle_type
#from mut4 import triangle_type
#from mut5 import triangle_type
import pytest

class TestTriangle:

    def test_equilateral(self):
        assert triangle_type(3, 3, 3) == 'Equilateral'

    def test_isosceles(self):
        assert triangle_type(3, 3, 2) == 'Isosceles'

    def test_scalene(self):
        assert triangle_type(3, 4, 5) == 'Scalene'

    def test_not_a_triangle(self):
        assert triangle_type(1, 2, 3) == 'Not a triangle'
