#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        // Convert entered key from string to integer type
        int key = atoi(argv[1]);

        string plain = get_string("Enter the code you want to encrypt:\n");

        printf("ciphertext: ");

        for (int n = 0; n < strlen(plain); n++)
        {
            // Check if plain character is a letter
            if (isalpha(plain[n]))
            {
                int ASCII = plain[n];

                // Process for uppercase character
                if (isupper(plain[n]))
                {
                    ASCII = ASCII - 65;
                    int aIndex = (ASCII + key) % 26;
                    ASCII = aIndex + 65;
                    printf("%c", ASCII);
                }

                // Process for lowercase character
                else if (islower(plain[n]))
                {
                    ASCII = ASCII - 97;
                    int aIndex = (ASCII + key) % 26;
                    ASCII = aIndex + 97;
                    printf("%c", ASCII);
                }

                // Simply print as character is if not a letter
            }
            else
            {
                printf("%c", plain[n]);
            }
        }
        printf("\n");
    }

    // If argc condition is not met
    else
    {
        return 1;
    }
}