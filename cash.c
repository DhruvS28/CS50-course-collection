#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float n;
    int c = 0;
    printf("Amount of change required:\n $ ");
    n = get_float();
    (n *= 100);

do
{
if (n >= 25)
    {
    n = n - 25;
    c = c + 1;
    }
else if (n < 25 && n >= 10)
    {
    n = n - 10;
    c = c + 1;
    }
else if (n < 10 && n >= 5)
    {
    n = n - 5;
    c = c + 1;
    }
else if (n < 5 && n >= 1)
    {
    n = n - 1;
    c = c + 1;
    }
}
while (n != 0);

printf("Minimum number of coins given: %i\n",c);
}