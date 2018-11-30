#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    //Stop if more than two aruments
    if (argc != 2)
    {
        {
            return 1;
        }
    }

    string pk = argv[1];

    //Stop if any characters in plain key not an alphabet
    for (int a = 0; a < strlen(pk); a++)
    {
        if (isalpha(pk[a]) == false)
        {
            return 1;
        }
    }

    string pt = get_string("Enter the code you want to encrypt:\n");
    printf("ciphertext: ");
    int j = 0, k;

    for (int i = 0; i < strlen(pt); i++)
    {
        // Check if plain character is a letter
        if (isalpha(pt[i]))
        {
            int a = pk[j];

            // Process for uppercase key character
            if (isupper(pk[j]))
            {
                k = a - 65;
            }

            // Process for lowercase key character
            else if (islower(pk[j]))
            {
                k = a - 97;
            }

            int ASCII = pt[i], aIndex;

            // Process for uppercase character
            if (isupper(pt[i]))
            {
                ASCII = ASCII - 65;
                aIndex = (ASCII + k) % 26;
                ASCII = aIndex + 65;
                printf("%c", ASCII);

                // Change value of j to be used for wraparound
                if (j < strlen(pk) - 1)
                {
                    j++;
                }
                else
                {
                    j = 0;
                }
            }
            // Process for lowercase character
            else if (islower(pt[i]))
            {
                ASCII = ASCII - 97;
                aIndex = (ASCII + k) % 26;
                ASCII = aIndex + 97;
                printf("%c", ASCII);

                // Change value of j to be used for wraparound
                if (j < strlen(pk) - 1)
                {
                    j++;
                }
                else
                {
                    j = 0;
                }
            }
        }
        // Simply print as character is if not a letter
        else
        {
            printf("%c", pt[i]);
        }
    }
    printf("\n");
}


