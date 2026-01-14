from calculator import Calculator
import pytest

class TestCalculator:

    def test_addition(self):
        self.calc = Calculator()
        assert self.calc.addition(2, 3) == 5
            
    def test_subtract(self):
        self.calc = Calculator()
        assert self.calc.subtract(5,2) == 3

    def test_division(self):
        self.calc = Calculator()
        assert self.calc.division(4,2) == 2

        with pytest.raises(ZeroDivisionError):
            self.calc.division(4,0)

    def test_multiply(self):
        self.calc = Calculator()
        assert self.calc.multiply(2,8) == 16