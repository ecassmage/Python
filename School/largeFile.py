from itertools import product
import time

if __name__ == "__main__":
    string = ""
    stringModify = ""
    append = "	-474938880\n"
    nums = 0
    length = 12000000
    chars = ["a", "b", "B"]
    start = time.time()
    file = open("largeFile.txt", "w")
    for gen in product(['a', 'b', 'B'], repeat=len("bBaabBbBbBaaaabBaabBbBbBaaaaaaaa")):
        if nums >= length:
            break

        if nums % 50000 == 0:
            print(f"{nums} and {time.time() - start}")
            # if time.time() - start > 1:
            start = time.time()
            file.write(string)
            string = ""

        string += "".join(gen) + append
        nums += 1

    print("We are here now")

    file.write(string)
    file.close()
