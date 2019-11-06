import unittest
from django_choices_enums.enum import DjangoChoicesEnum


class MyEnum(DjangoChoicesEnum):
    A = (1, 'xxx')
    B = (2, 'xxx')


class MyEnum2(DjangoChoicesEnum):
    A = (1, 'xxx')
    B = (2, 'xxx')

    anonymous = ((3, 'xx'),
                 (4, 'xx'),
                 )


class MyEnumVerbose(DjangoChoicesEnum):
    A = (12, 'test')
    B = (1, 'B')
    anonymous = ((32, 'anonymous_32'),
                 (4, 'xx'),
                 )


class TestAddCount(unittest.TestCase):
    def test_1(self):
        a = MyEnum.A
        self.assertEqual(a, 1)

        values = MyEnum.all_values()

        self.assertEqual(values, [1, 2])

    def test_2(self):
        self.assertEqual(MyEnum2.to_django_choices(), [(1, 'xxx'), (2, 'xxx'), (3, 'xx'), (4, 'xx')])
        self.assertEqual(MyEnum2.all_values(), [1, 2, 3, 4])

    def test_verbose(self):
        self.assertEqual(MyEnumVerbose.A.verbose, 'test')
        self.assertEqual(MyEnumVerbose.get_verbose(MyEnumVerbose.B), 'B')
        self.assertEqual(MyEnumVerbose.get_verbose(1), 'B')

        self.assertEqual(MyEnumVerbose.get_verbose(32), 'anonymous_32')
