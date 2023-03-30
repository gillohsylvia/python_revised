#include <stdio.h>
/* #include "main.h"/*

/* function to print square */
/**
 * print_square - print a square of # size
 * @size: size to draw
*/

int print_square(int size)
{
    int row, column;

    if (size > 0)
    {
        for (row = 1; row <= size; row++)
        {
            for (column = 1; column <= size; column++)
            {
                printf("#");
            }
            printf("#");
        }
    }
    else
        printf("\n");
}

