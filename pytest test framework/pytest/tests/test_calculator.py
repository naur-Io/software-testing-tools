from calculator import Calculator
import pytest
from random import randint as randInt

def get_data(calc):
    inputs = []
    for i in range(calc):
        a = randInt(1, 100)
        b = randInt(1, 100)
        result = a + b
        inputs.append((a, b, result))
    return inputs


class TestCalculator:

    # Setup method to initialize Calculator instance before tests
    def setup_class(self):
        print("Setup Calculator")
        self.calc = Calculator()

    def setup_method(self):
        print(f"executed before each test.") 
         
    def teardown_class(self):
        print("\n Teardown Calculator")
        del self.calc
    
    def test_addition(self):
        assert self.calc.addition(2,3) == 5
            
    def test_subtract(self):
        assert self.calc.subtract(5,2) == 3

    def test_division(self):
        assert self.calc.division(4,2) == 2

    def test_multiply(self):
        assert self.calc.multiply(3,4) == 12

    def test_sumWithStirng(self):
        with pytest.raises(TypeError):
            self.calc.addition(5, "test")

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(10, 0)
   
    @pytest.mark.skip(reason="duplicate test case")
    def test_addition_duplicate(self):
        assert self.calc.addition(2,3) == 5

    @pytest.mark.skipif(True, reason="Skipping this test")
    def test_subtract_skipif(self):
        assert self.calc.subtract(5,2) == 3

    @pytest.mark.xfail(reason="power method not implemented yet")
    def test_power(self):
        assert self.calc.power(2, 3) == 8

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 6),  
        (4, 5, 20), 
        (0, 10, 0), 
        (5, 5, 25), 
        (7, 2, 14) 
    ])
    def test_multiplication_parametrized(self, a, b, expected):
        assert self.calc.multiply(a, b) == expected
    
    @pytest.mark.parametrize("a, b, expected", get_data(1000))
    def test_addition_many(self, a, b, expected):
        assert self.calc.addition(a, b) == expected