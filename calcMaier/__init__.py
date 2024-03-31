from ._exceptions import *

class CalculatorMaier:
    @staticmethod
    def add_numbers(a: float, b: float):
        if not (isinstance(a, float) and isinstance(b, float)):
            raise CalcException("Wrong DataType")
        return a + b
    @staticmethod
    def subtrakt_numbers(a: float, b: float):
        if not (isinstance(a, float) and isinstance(b, float)):
            raise CalcException("Wrong DataType")
        return a - b