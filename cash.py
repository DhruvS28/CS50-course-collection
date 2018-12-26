import cs50


def main():
    # While loop to only accept positve values for change required
    while True:
        n = cs50.get_float("Amount of change required:\n$ ")
        if n > 0:
            break
    # Converting change from dollars to cents
    n *= 100
    n = round(n)
    c = 0

    # While loop to count coins and decreases the change required corresponding to the coin amount used
    while True:
        if n >= 25:
            n = n - 25
            c = c + 1
        elif n < 25 and n >= 10:
            n = n - 10
            c = c + 1
        elif n < 10 and n >= 5:
            n = n - 5
            c = c + 1
        elif n < 5 and n >= 1:
            n = n - 1
            c = c + 1
        # Breaks loop as when change required reaches 0
        else:
            break

    print(f"Minimum number of coins given: {c}")


if __name__ == "__main__":
    main()