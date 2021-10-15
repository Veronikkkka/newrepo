def total_occurrences(s1, s2, ch):
    """
    (str, str, str) -> int
    Precondition: len(ch) == 1
    Return the total number of times that ch occurs in s1 and s2.
    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')
    1
    >>> total_occurrences('green', 'purple', 'b')
    0
    """
    k = 0
    if isinstance(s1, str) and isinstance(s2, str) and isinstance(ch, str) and len(ch) == 1:
        for i in s1:
            if i == ch:
                k += 1
        for i in s2:
            if i == ch:
                k += 1
        return k
print(total_occurrences('red', 'blue', 'e'))
