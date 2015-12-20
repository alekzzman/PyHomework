def overlapping(a, b):
    """
    Task:
    Define a function overlapping() that takes
    two lists and returns True if they have at
    least one member in common, False otherwise.
    You may use your is_member() function, or the
    in operator, but for the sake of the exercise,
    you should (also) write it using two nested for-loops.
    >>> overlapping(a = [1,12,53,66,78,35,236], b = [2,15,84,31,36,25,236])
    True
    """
    result = False
    for numa in a:
        for numb in b:
            if numa == numb:
                result = True
    print(result)