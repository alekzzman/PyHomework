def reverse(text):
    """
    Define a function reverse() that computes
    the reversal of a string. For example,
    reverse("I am testing") should return the
    string "gnitset ma I"
    >>> z = reverse(text)
    >>> x = text[::-1]
    >>> z == x
    True
    """
    listed = list(text)
    firstchar = 0
    lastchar = len(listed) - 1
    while firstchar < lastchar:
        listed[firstchar], listed[lastchar] = listed[lastchar],listed[firstchar]
        firstchar += 1
        lastchar -= 1
    result = ''.join(listed)
    return result
reverse('i am testing')