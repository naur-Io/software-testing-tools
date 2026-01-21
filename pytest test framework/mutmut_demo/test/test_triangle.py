from src.triangle import triangle_type

def test_equilateral():
    assert triangle_type(3, 3, 3) == 'Equilateral'

def test_isosceles_ab():
    assert triangle_type(3, 3, 2) == 'Isosceles'

def test_isosceles_ac():
    assert triangle_type(3, 2, 3) == 'Isosceles'

def test_isosceles_bc():
    assert triangle_type(2, 3, 3) == 'Isosceles'

def test_scalene():
    assert triangle_type(3, 4, 5) == 'Scalene'

def test_scalene_permutation():
    assert triangle_type(5, 3, 4) == 'Scalene'

def test_not_triangle_limit():
    assert triangle_type(1, 2, 3) == 'Not a triangle'

def test_not_triangle_sum_less():
    assert triangle_type(1, 1, 3) == 'Not a triangle'

def test_degenerate_triangle():
    assert triangle_type(2, 2, 4) == 'Not a triangle'

def test_zero_side():
    assert triangle_type(0, 2, 2) == 'Not a triangle'

def test_negative_side():
    assert triangle_type(-1, 2, 2) == 'Not a triangle'

def test_soma_vs_subtracao():
    assert triangle_type(5, 3, 3) == "Isosceles"

def test_triangle_equality_border_specific():
    assert triangle_type(3, 4, 7) == "Not a triangle"

def test_all_equal_but_not_triangle():
    assert triangle_type(1, 1, 2) == "Not a triangle"

def test_isosceles_minimal_valid():
    assert triangle_type(2, 2, 3) == "Isosceles"

def test_equilateral_minimal():
    assert triangle_type(1, 1, 1) == "Equilateral"

def test_triangle_border_a_c_equals_b():
    assert triangle_type(2, 4, 2) == "Not a triangle"

def test_triangle_border_b_c_equals_a():
    assert triangle_type(4, 2, 2) == "Not a triangle"


