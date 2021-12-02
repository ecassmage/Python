x = -15.641  # This is -15.641 assigned to x
print(f"This is x: {x}")  # This prints x

y = 38  # This is 38 assigned to x
print(f"This is y: {y}")  # This prints y

rounded = round(x, 0)  # This is -15.641 rounded to the nearest unit as rounds default overloaded value  // can also be round(x, 0), this will make rounded a float point variable over round(x) making it an int.
print(f"This is rounded: {rounded}")  # This prints rounded

absoluteVal = abs(rounded)  # This is the absolute value of rounded.
print(f"This is absoluteVal: {absoluteVal}")  # This prints absoluteVal

remainder = y % 11  # This calculates the remainder of y
print(f"This is remainder: {remainder}")  # This prints remainder

result = round(pow(x, 3) - (4 * x) + 19, 3)  # This is a quadratic equation with x being the variable x
print(f"This is result: {result}")  # This prints result

intresult = int(result)  # This is result being casted from a floating point to an integer
print(f"This is intresult: {intresult}")  # This prints intresult
