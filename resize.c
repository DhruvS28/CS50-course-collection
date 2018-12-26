#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 4)
    {
        printf("Usage: ./resize n infile outfile\n");
        return 1;
    }

    // Remember filenames and assign scale change as integer
    int n = atoi(argv[1]);
    char *infile = argv[2];
    char *outfile = argv[3];

    if (n <= 0 || n > 100)
    {
        printf("Usage: 0 <= n < 100\n");
        return 1;
    }

    // Open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        printf("Could not open %s.\n", infile);
        return 2;
    }

    // Open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }

    // Create new BITMAPFILEHEADER and BITMAPINFOHEADER
    BITMAPFILEHEADER nbf = bf;
    BITMAPINFOHEADER nbi = bi;

    // Rescale dimensions for outfile with n
    nbi.biWidth *= n;
    nbi.biHeight *= n;

    // Determine original and new padding for scanlines
    int padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    int newpadding = (4 - (nbi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    // Determine the outfile biSizeImage and bfSize
    nbi.biSizeImage = abs(nbi.biHeight) * (nbi.biWidth * sizeof(RGBTRIPLE) + newpadding);
    nbf.bfSize = (nbi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER));

    // Write outfile's BITMAPFILEHEADER
    fwrite(&nbf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // Write outfile's BITMAPINFOHEADER
    fwrite(&nbi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // Iterate over infile's scanlines
    for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++)
    {
        for (int j = 0; j < n; j++)
        {
            // Set pointer to beginning of line
            fseek(inptr, 54 + (bi.biWidth * 3 + padding) * i, SEEK_SET);

            // Iterate over pixels in scanline
            for (int m = 0; m < bi.biWidth; m++)
            {
                // Temporary storage
                RGBTRIPLE triple;

                // Read RGB triple from infile
                fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

                // Write RGB triple to outfile n times
                for (int l = 0; l < n; l++)
                {
                    fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                }
            }

            // Then add it back
            for (int k = 0; k < newpadding; k++)
            {
                fputc(0x00, outptr);
            }
        }
    }

    // Close infile
    fclose(inptr);

    // Close outfile
    fclose(outptr);

    return 0;
}