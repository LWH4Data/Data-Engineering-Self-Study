#include <stdio.h>

int main()
{
    int minInt1 = -2147483648LL;
    int underflow1 = minInt1 - 1;

    printf("minInt: %d\n", minInt1);
    printf("underflow1: %d\n", underflow1);

    unsigned int minInt2 = 0;
    unsigned int underflow2 = minInt2 - 1;

    printf("minInt: %d\n", minInt2);
    printf("underflow2: %u\n", underflow2);

    return 0;
}