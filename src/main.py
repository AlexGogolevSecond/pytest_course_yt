from typing import Union


class Calculator:
    def devide(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        return x / y

    def add(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        return x + y

# class A:
#     x = 1


if __name__ == '__main__':
    calculator = Calculator()
