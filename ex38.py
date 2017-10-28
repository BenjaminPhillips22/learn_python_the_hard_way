ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list,let's fix that.")

stuff = ten_things.split(" ")
more_stuff = "Day Night Song Frisbee Corn Banana Girl Boy".split(" ")

while len(stuff) != 10:
    stuff.append(more_stuff.pop())
    print(f"There's now {len(stuff)} things in stuff")

print("There we go:", stuff)

print("# ".join(stuff))
