alphabet = 'abcdefghijklmnopqrstuvwxyz'

def check(text):
    return set(text.lower()).issuperset(set(alphabet))   