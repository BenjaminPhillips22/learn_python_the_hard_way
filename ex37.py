# %%

# Symbol Review
try:
    assert False, "My cool error message!"
except AssertionError:
    print("a second error message.")


# %%

# to delete and item from a dictionary, use del

cool_dict = {'a': 1, 'b': 'cool', 'c': [3, 3]}
del cool_dict['b']
print(cool_dict)

# %%

foo_2 = lambda x, y: x + y
print(foo_2(3, 2))
