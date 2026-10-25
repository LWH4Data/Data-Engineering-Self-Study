#include <stdio.h>

int main()
{
    signed short smallest_short = -32768;
    signed short largest_short = 32767;

    signed int smallest_int = -2147483648;
    signed int largest_int = 2147483647;

    printf("signed short: %d ~ %d\n", smallest_short, largest_short);
    printf("signed int: %d ~ %d\n", smallest_int, largest_int);

    return 0;
}