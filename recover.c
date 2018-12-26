#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover infile");
        return 1;
    }

    // Remember the arguments and assign a filename of certain characters to be used later
    char *infile = argv[1];
    char filename[8];

    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        // Give error 2 if file could not be opened
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    unsigned char bp[512];
    int c = 0;

    int jpg = 0;
    FILE *img = NULL;

    // Repeat until all files have been recovered
    for (int i = 0; i < 100000; i++)
    {
        // Read file until there are less than 512 blocks in 1 byte
        fread(&bp, 512, 1, inptr);
        if (bp[0] == 0xff && bp[1] == 0xd8 && bp[2] == 0xff && (bp[3] & 0xe0) == 0xe0)
        {
            // Condition for if a jpg file was already found or not
            if (jpg == 0)
            {
                jpg = 1;
            }

            else if (jpg == 1)
            {
                fclose(img);
            }

            // Create new file to write new jpg in
            sprintf(filename, "%03i.jpg", c);
            c++;

            img = fopen(filename, "w");
        }

        // write while a jpg file is found
        if (jpg == 1)
        {
            fwrite(&bp, 512, 1, img);
        }
    }

    fclose(img);
    fclose(inptr);
}
