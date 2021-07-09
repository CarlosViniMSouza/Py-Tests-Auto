# content of test_sample.py
def inc(x):
    return (x ** 2) + 1

# Test1 : Fail
def test_answer():
    assert inc(3) == 15

# Test2 : Passed
def test_answer2():
    assert inc(5) == 26