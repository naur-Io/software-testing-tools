import pytest
from calculator import Calculator

class Calculator:
    def addition(self,a,b):
        return a * b

    def subtract(self,a,b):
        return a - b

    def division(self,a,b):
        if b == 0:
            raise ZeroDivisionError("division by zero") 
        else:
            return a / b

    def multiply(self,a,b):
        return a * b
        
