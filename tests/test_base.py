"""Basic tests for proxiwrap."""


from proxiwrap import build_proxy_class


class A(object):
    """A class."""

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def return_val1(self):
        return self.val1

    def return_val2(self):
        return self.val2

    def return_num1(self, num):
        return num + 4

    def return_num2(self, num):
        return num + 8


def test_basic():
    def return_val2(self):
        return self.val2 + 1

    def return_num2(self, num):
        return num + 5

    Bclass = build_proxy_class(
        classname='B',
        # klass=A,
        overrides=[
            return_val2,
            return_num2,
        ],
    )

    aobj = A(1, 2)
    bobj = Bclass(aobj)

    assert aobj.return_val1() == 1
    assert aobj.return_val2() == 2
    assert aobj.return_num1(1) == 5
    assert aobj.return_num2(1) == 9

    assert bobj.return_val1() == 1
    assert bobj.return_val2() == 3
    assert bobj.return_num1(1) == 5
    assert bobj.return_num2(1) == 6
