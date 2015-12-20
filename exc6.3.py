def is_member(val, lst):
    """
    Task:
    Write a function is_member() that takes
    a value (i.e. a number, string, etc) x
    and a list of values a, and returns True
    if x is a member of a, False otherwise.
    (Note that this is exactly what the in operator
    does, but for the sake of the exercise you
    should pretend Python did not have this operator.)
    >>> is_member(val = 75, lst = [2, 1, 4, 5, 3, 12, 25, 75])
    True
    """
    n = 0
    result = False
    try:
        while True:
            if val == lst[n]:
                result = True
                break
            else:
                n += 1
    except:
        result = False
    return print(result)