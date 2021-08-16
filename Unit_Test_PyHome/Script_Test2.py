import unittest

def calculator():
    op1 = 10 + 15
    op2 = 15 - 9
    op3 = 12 / 6
    result = [op1, op2, op3]
    return result

myList = calculator()

class MyTestCase(unittest.TestCase):

    def test_res1(self):
        self.assertEqual(6, myList[1])


if __name__ == '__main__':
    unittest.main()
