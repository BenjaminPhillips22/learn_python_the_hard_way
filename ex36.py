def bank(current_dollars, deposit):
    return current_dollars - deposit


def youth_centre(current_age, years_off):
    return current_age - years_off


print("--------------------")

name = input("What's your name?\n> ")

print(f"Nice to meet you {name}.")

age = int(input("How old are you?\n> "))
dollars = int(input("How many dollars do you have?\n> "))

while True:
    print("""
    Would you like to win the game? (press 'a')
    Would you like to go to the bank? (press 'b')
    Would you like to go to the youth centre? (press 'c')""")
    choice = input("> ")

    if choice == 'a':
        condition = age*2 == dollars
        if condition:
            print("You win the game!")
            exit(0)
        else:
            print("""To win the game,
            you need two dollars for every year that you have lived""")
    elif choice == 'b':
        print("How much money will you deposit?")
        money_to_deposit = int(input("> "))
        dollars = bank(current_dollars=dollars, deposit=money_to_deposit)
        print(f"You now have {dollars} dollars.")
    elif choice == 'c':
        print("How many years would you like to lose?")
        years_to_lose = int(input("> "))
        age = youth_centre(current_age=age, years_off=years_to_lose)
        print(f"You are now {age} years old.")
    else:
        print("You lose!")
        exit(0)
