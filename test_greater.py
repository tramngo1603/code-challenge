from immediate_greatest import findGreater

def test_myfunc1():
    result1 = findGreater(12345967)
    assert result1 == 12345976

def test_myfunc2():
    result1 = findGreater(54321)
    assert result1 == 54321

def test_myfunc3():
    result1 = findGreater(78960231)
    assert result1 == 78960312

def test_singledigit():
    result1 = findGreater(3)
    assert result1 == 3
