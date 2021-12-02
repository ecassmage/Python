def volume(r, h) -> float:
    return round(3.14 * (r ** 2) * h, 2)  # returns the volume of the inputted cylinder.


if __name__ == '__main__':
    radius = float(input("Please enter a radius value which is positive: "))  # takes a str and converts it to float. Assumes the input is positive which means valid.
    height = float(input("Please enter a height value which is positive: "))  # takes a str and converts it to float. Assumes the input is positive which means valid.
    result = volume(radius, height)  # calculates volume in O(1)
    print(f"The volume of a cylinder with radius {radius} cm and height {height} cm is {result} cm^3")  # prints a suitable message which is an exact copy of the example in the lab.
