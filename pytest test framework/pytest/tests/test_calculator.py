from calculator import Calculator
import pytest


class TestCalculator:

    # Setup method to initialize Calculator instance before tests
    def setup_class(self):
        print("Setup Calculator instance for all tests.")
        self.calc = Calculator()

    def setup_method(self):
        print(f"executed before each test.") 
         
    def teardown_class(self):
        print("\nTeardown Calculator instance after tests.")
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

    @pytest.mark.skipif(True, reason="Skipping this test unconditionally")
    def test_subtract_skipif(self):
        assert self.calc.subtract(5,2) == 3


