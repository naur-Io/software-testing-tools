
class Calculator:
    def addition(self,a,b):
        return a + b

    def subtract(self,a,b):
        return a - b

    def division(self,a,b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a/b

    def multiply(self,a,b):
        return a * b