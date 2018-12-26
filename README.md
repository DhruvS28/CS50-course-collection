# Questions

## What's `stdint.h`?

stdint.h is a library included to help one make and structure their own data types.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

uint refers so an unsigned integer (BYTE, DWORD & WORD), while reffers just int reffers to a signed integer (LONG).
The number mentioned refers to how many bits are allocated.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE: 1 byte, DWORD: 4 bytes, LONG: 4 bytes, WORD: 2 bytes.

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

4d bytes & 42 bytes. Hence, 0x4d42 in hexadecimal. (Line 47 in the code)

## What's the difference between `bfSize` and `biSize`?

biSize, present in 'BITMAPINFOHEADER', contains the total size of the image, including padding. 40 bytes.
bfSize, present in 'BITMAPFILEHEADER', contains the total size of the file, including padding, pixels & headers. 14 bytes.

## What does it mean if `biHeight` is negative?

biHeight contains the height of the image.
The image would origin from the upper left corner if biHeight was negative, rather than lower left corner if positive.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

The field biBitCount specifes such.

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

'NULL' would be returned if the file to be read or write in is not present, respectively for lines 24 and 32.

## Why is the third argument to `fread` always `1` in our code?

The third argument implies how many elements must be read.
Since, the code copies a singular .bmp file, only one file is required to be read.

## What value does line 65 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

Padding would be assigned assigned the value 1.
biWidth = 3 pixels, scanline must be a multiple of 4 pixels. Hence 4 - 3 = 1.

## What does `fseek` do?

It helps move the file position indicator by a set amount of bytes from a specific location in the file.

## What is `SEEK_CUR`?

One of the specific locations used in the fseek function.
Used to move the file position indicator by a set amount from the current possition in the file

## Whodunit?

It was Professor Plum with the candlestick in the library.
