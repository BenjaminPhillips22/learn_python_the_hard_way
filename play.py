def isTwo(num):
    if num == 2:
        return True
    return False


# test
print(isTwo(2))

print(isTwo(9))


def do_a_thing(x, *, bool=True):
    if bool:
        return x
    return x**2


print(do_a_thing(2, bool=False))
