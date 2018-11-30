// Helper functions for music

#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

#include "helpers.h"

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    // Converting fractions to integers to further convert to eights
    int num = fraction[0] - '0';
    int denom = fraction[2] - '0';

    int d = (8 / denom) * num;
    return d;
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    // Process to fnd what the octave is
    int oct = note[strlen(note) - 1] - '0';

    double f = 0.0;

    // Process that considers which key the note is
    if (note[0] == 'A')
    {
        f = 440.0;
    }

    // Multiplied here as B note in the same octave is one semitone higher than A
    else if (note[0] == 'B')
    {
        f = 440.0 * pow(2.0, (2.0 / 12.0));
    }

    // Divded from C to G as these notes in the same octave are a set amount of semitones lower than A
    else if (note[0] == 'C')
    {
        f = 440.0 / pow(2.0, (9.0 / 12.0));
    }

    else if (note[0] == 'D')
    {
        f = 440.0 / pow(2.0, 7.0 / 12.0);
    }

    else if (note[0] == 'E')
    {
        f = 440.0 / pow(2.0, 5.0 / 12.0);
    }

    else if (note[0] == 'F')
    {
        f = 440.0 / pow(2.0, 4.0 / 12.0);
    }

    else if (note[0] == 'G')
    {
        f = 440.0 / pow(2.0, 2.0 / 12.0);
    }

    // Process that considers which octave the key is
    if (oct > 4.0)
    {
        int i = pow(2.0, oct - 4);
        f *= i;
    }

    else if (oct < 4.0)
    {
        int i = pow(2.0, 4 - oct);
        f /= i;
    }

    // Process that considers whether note is a sharp or flat
    if (note[1] == '#')
    {
        f *= pow(2.0, 1.0 / 12.0);
    }

    else if (note[1] == 'b')
    {
        f /= pow(2.0, 1.0 / 12.0);
    }

    int freq = round(f);
    return freq;
}



// Determines whether a string represents a rest
bool is_rest(string s)
{
    // Check for whether the line is completely blank with the \0 value
    if (s[0] != '\0')
    {
        return false;
    }

    else
    {
        return true;
    }
}