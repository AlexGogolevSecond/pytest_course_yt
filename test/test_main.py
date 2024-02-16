# from src.main import A


# def test_main():
#     assert A.x == 1

# def test_2():
#     assert 2 == 2


# def test_sum():
#     x = 3
#     y = 2
#     assert x + y == 5


from src.main import Calculator
import pytest


# def test_divide():
#     x = 1
#     y = 2
#     res = 0.5
#     assert Calculator().devide(x, y) == res

@pytest.mark.parametrize(
        'x, y, res',
        [
            (1, 2, 0.5),
            (1, 1, 1),
            (5, -1, -5)
        ]
    )
def test_divide(x, y, res):
    assert Calculator().devide(x, y) == res


@pytest.mark.parametrize(
        'x, y, res',
        [
            (1, 2, 3),
            (1, 1, 2),
            (5, -1, 4)
        ]
    )
def test_add(x, y, res):
    assert Calculator().add(x, y) == res