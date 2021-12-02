if __name__ == '__main__':  # guard.
    x = int(input("Enter a valid positive integer > 0: "))  # takes an int as input assumes valid input.
    # should have written the comments at same time Kind of confusing myself with my terrible code.
    added = 0  # collects up all divisors excluding itself.
    print(f"The positive divisors of {x} are:")  # Styling print for explaining importance of subsequent numbers.
    # originally had x + 1 then removed x from added in the if added = x line. I do dumb stuff sometimes.
    for n in range(1, x):  # goes through numbers between 1 (inclusive) and x (exclusive). More efficient ways but since small data set, efficient code is unnecessary.
        if x % n == 0:  # checks remainder of x / n. If 0 remainder then do this.
            added += n  # adds successful divisor to added.
            print(n)  # prints a successful divisors.
    # could unify the rest into a single line however I am lazy.
    if added == x:  # This removes itself.
        print(f"{x} is a perfect number")  # prints message if perfect number.
    else:  # else do this.
        print(f"{x} is not a perfect number")  # prints message if not perfect number.
