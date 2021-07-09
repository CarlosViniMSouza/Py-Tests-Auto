import unittest
import pytest


class MyTestCase(unittest.TestCase):
    # content of test_50.py
    @pytest.mark.parametrize("i", range(50))
    def test_num(i):
        if i in (17, 25):
            pytest.fail("bad luck")

if __name__ == '__main__':
    unittest.main()
