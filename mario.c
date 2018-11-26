#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n, a = 0, b = 0, c = 0;
do
{
    printf("How many layers should the pyramid have?\n");
    n = get_int();

}
while (n < 0 || n > 23);
int d = n;

    for (c = 0; n > c; n-- )
{
    for (a = 0; a < n - 1 ; a++ )
    {
    printf(" ");
    }

    for (b = 0; b < d - a ; b++ )
    {
    printf("#");
    }
    {
        printf("  ");
    }

    for (b = 0; b < d - a ; b++ )
    {
    printf("#");
    }

        {
        printf("\n");
        }
}

}


