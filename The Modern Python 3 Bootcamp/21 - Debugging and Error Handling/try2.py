while True:
    try:
        num = int(input("Please enter a number: "))
    except ValueError:
        print("Thats not a number!")
    else:
        print("Good job, you entered a number!")
        break
    finally:
        print("Runs NO matter what!")
print("REST of game logic runs!")