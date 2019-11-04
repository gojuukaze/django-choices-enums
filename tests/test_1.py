from django_choices_enum import DjangoChoicesEnum


class MyEnum(DjangoChoicesEnum):
    A = (1, 'xxx')
    B = (2, 'xxx')


def test_enum():
    a = MyEnum.A
    assert a == 1

    values = MyEnum.all_values()

    assert values == [1, 2]


if __name__ == '__main__':
    test_enum()
