import cs50


def main():
    # Emulating a do-while loop from C
    while True:
        n = cs50.get_int("How many layers should the pyramid have? ")
        if n >= 0 and n <= 23:
            break

    for c in range(n):
        # Printing the required number of spaces
        n = n - 1
        for a in range(n):
            print(" ", end="")
        # Printing the required number of blocks with spaces, and the remaining same number of blocks
        for b in range(c + 1):
            print("#", end="")
        print("  ", end="")
        for b in range(c + 1):
            print("#", end="")
        print("")


if __name__ == "__main__":
    main()