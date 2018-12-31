// Implements a dictionary's functionality

#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "dictionary.h"


typedef struct node
{char word[LENGTH + 1];
    struct node *next;}
node;

int s = 10;

node *ht[10] = {NULL};


int hash(const char *word)
{
    int hash = 0;
    int n;
    for (int i = 0; word[i] != '\0'; i++)
    {
        if (isalpha(word[i]))
        {
            n = word [i] - 'a' + 1;
        }
        else
        {
            n = 27;
        }
        hash = ((hash << 3) + n) % s;
    }
    return hash;
}


int disi = 0;

//Loads dictionary into memory.  Returns true if successful else false.
bool load(const char *dictionary)
{
    FILE *di = fopen(dictionary, "r");
    if (di == NULL)
    {
        return false;
    }
    char word[LENGTH + 1];

    while (fscanf(di, "%s\n", word) != EOF)
    {
        disi++;
        node *node1 = malloc(sizeof(node));
        strcpy(node1->word, word);
        int index = hash(word);

        if (ht[index] == NULL)
        {
            ht[index] = node1;
            node1->next = NULL;
        }
        else
        {
            node1->next = ht[index];
            ht[index] = node1;
        }
    }
    fclose(di);
    return true;
}

// Returns true if word is in dictionary else false.
bool check(const char *word)
{
    char temp[LENGTH + 1];
    int len = strlen(word);
    for (int i = 0; i < len; i++)
    {
        temp[i] = tolower(word[i]);
    }
    temp[len] = '\0';

    int index = hash(temp);

    if (ht[index] == NULL)
    {
        return false;
    }

    node *cursor = ht[index];

    while (cursor != NULL)
    {
        if (strcmp(temp, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded.
unsigned int size(void)
{
    if (disi >= 0)
    {
        return disi;
    }
    return true;
}

// Unloads dictionary from memory.  Returns true if successful else false.
bool unload(void)
{
    for (int index = 0; index < s; index++)
    {
        while (ht[index] != NULL)
        {
            node *cursor = ht[index];
            ht[index] = cursor->next;
            free(cursor);
        }
    }
    return true;
}