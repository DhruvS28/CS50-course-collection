from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # Returns each different line of two different strings
    a1 = set(a.splitlines())
    b2 = set(b.splitlines())

    return a1 & b2


def sentences(a, b):
    """Return sentences in both a and b"""

    # Returns proper sentences that may be detected in each string
    a3 = set(sent_tokenize(a))
    b4 = set(sent_tokenize(b))

    return a3 & b4


def subs(str, n):
    subs = []

    # Added function to be used for substrings
    for i in range(len(str) - n + 1):
        subs.append(str[i:i + n])

    return subs


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # Returns the substrings of each full string
    a5 = set(subs(a, n))
    b6 = set(subs(b, n))

    return a5 & b6