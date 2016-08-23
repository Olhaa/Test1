from string import ascii_lowercase as az


def check(text):
    return set(text.lower()).issuperset(set(alphabet))

print(check('abc'))