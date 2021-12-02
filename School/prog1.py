if __name__ == "__main__":
    num = None
    try:
        num = float(input("Please enter a number: "))
    except ValueError:
        print("That wasn't even a number")
        exit()
    if num > 0:
        print(f"This number is positive: {num}")
    elif num == 0:
        print(f"This number is {num} so I am not sure what to do with it since 0 is neither positive or negative")
    else:
        print("That Number was not positive")
