from unittest import expectedFailure

from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class BinTests(TranspileTestCase):
    @expectedFailure
    def test_int_but_no_index(self):
        self.assertCodeExecution("""
            class IntLike:
                def __init__(self, val):
                    self.val = val
                def __int__(self):
                    return self.val

            x = IntLike(5)
            print(bin(x))
            """)


class BuiltinBinFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["bin"]

    not_implemented = [
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_complex',
        'test_dict',
        'test_frozenset',
        'test_set',
    ]
