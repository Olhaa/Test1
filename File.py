from string import ascii_lowercase as az


def check(text):
    return set(text.lower()).issuperset(set(az))

print(check('abc') == False)
print(check('abcdefghijklmnopqrstuvwxyz') == True)
print(check('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == True)
print(check('Quick brown fox jumped over the lazy dog') == True)