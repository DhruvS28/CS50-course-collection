import sys
import cs50


def main():
    if len(sys.argv) != 2:
        # Exit out of the program with '1' if there are not two command line arguments
        sys.exit(1)
    else:
        # Convert the key entered to an integer value and prompt what must be enxrypted
        key = int(sys.argv[1])
        plain = cs50.get_string("Enter the code you want to encrypt:\n")
        print("ciphertext: ", end="")

        for x in plain:
            # Check for whether the character is alphabetical
            if x.isalpha() == True:
                # Convert letter to its ASCII value
                ASCII = ord(x)
                # Check if character is uppercase or lowercase
                if x.isupper() == True:
                    ASCII = ASCII - 65
                    aIndex = (ASCII + key) % 26
                    ASCII = aIndex + 65
                    print(chr(ASCII), end="")
                elif x.islower() == True:
                    ASCII = ASCII - 97
                    aIndex = (ASCII + key) % 26
                    ASCII = aIndex + 97
                    print(chr(ASCII), end="")
            # If not alphabetical, print as it is
            else:
                print(x, end="")
        print()


if __name__ == "__main__":
    main()