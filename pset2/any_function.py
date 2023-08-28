# this is an example of the any function

def is_there(text):
    chars_to_check = "'.,;:?! "
    for c in text:
        if c in chars_to_check:
            return True
    return False

def alter_ego(text):
    chars_to_check = "'.,;:?! "
    return any(c in chars_to_check for c in text)

print(is_there("hello"))
print(is_there("hel.lo"))
print()
print(alter_ego("hello"))
print(alter_ego("hel.lo"))