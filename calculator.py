class Calculator:
    __result = 0
    def __init__(self):
        pass

    def add(self, a):
        self.__result += a

    def subtract(self, a):
        self.__result -= a

    def multiply(self, a):
        self.__result *= a

    def divide(self, a):
        if a == 0:
            raise ValueError("cannot divide by zero")
        self.__result /= a

    def modulo(self, a):
        if a == 0:
            raise ValueError("cannot divide by zero")
        self.__result %= a

    def power(self, a):
        self.__result **= a

    def square_root(self):
        self.__result **= 0.5
        

    def clear(self):
        self.__result = 0

    def get_result(self):
        return self.__result
