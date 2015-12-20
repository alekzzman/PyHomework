"""
Task:
Define a function is_palindrome() that
recognizes palindromes (i.e. words that
look the same written backwards). For
example, is_palindrome("radar") should
return True
>>> text = 'radar'
>>> is_palindrome(text)
True
"""
def is_palindrome(text):
    listed = list(text)
    a = len(listed) - 1
    b = 0
    while b < a:
        if listed[b] == listed[a]:
            x = True
        else:
            x = False
            break
        b += 1
        a -= 1
    return print(x)
is_palindrome('radar')
