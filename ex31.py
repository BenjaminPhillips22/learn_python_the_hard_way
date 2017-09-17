print("""You enter a room.
There is a chair in the room.
There is a door in the room.""")

print("""Do you sit on the chair (press '1')
or go through the door (press '2')""")

choice = input("> ")

if choice == '1':
    print("The chair is an illusion, you fall on your bum")
elif choice == '2':
    print("The door is just a painting on the wall.")
else:
    print("No choice is still a choice.")

print("""You begin to understand the situation you're in.
Do you try leave the way you came in (press 'a') or
do you start to think of a cunning plan (press 'b')""")

choice = input("> ")

print("You're choice is irrelevant and life has no meaning")
