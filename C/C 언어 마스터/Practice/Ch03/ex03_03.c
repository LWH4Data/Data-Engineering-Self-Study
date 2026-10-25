#include <stdio.h>

int main()
{
    int maxInt = 2147483647;
    int overflow1 = maxInt + 1;

    printf("maxInt: %d\n", maxInt);
    printf("overflow1: %d\n", overflow1);

    unsigned int maxUnit = 4294967295U;
    unsigned int overflow2 = maxUnit + 1;

    printf("macUnit: %u\n", maxUnit);
    printf("overflow2: %u\n", overflow2);

    return 0;
}