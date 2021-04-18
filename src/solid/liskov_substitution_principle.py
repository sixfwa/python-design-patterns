"""
Liskov's Substitution Principle

Let Φ(x) be a property provable about objects x of type T. 
Then Φ(y) should be true for objects y of type S where S 
is a subtype of T.

Child class objects should be able to replace parent class objects
without breaking the integrity of the application.
"""


class Calculator:
    @staticmethod
    def calculate(number_one, number_two):
        return number_one * number_two


class DividerCalculator(Calculator):
    @staticmethod
    def calculate(number_one, number_two):
        return number_one / number_two


if __name__ == "__main__":
    print(Calculator.calculate(4, 3))
    print(DividerCalculator.calculate(12, 3))
    print(DividerCalculator.calculate(12, 0))