#include <stdio.h>

int main()
{
    float x, y;

    printf("밑변: ");
    scanf("%f", &x);

    printf("높이: ");
    scanf("%f", &y);

    printf("넓이: %.1f", (x * y) / 2);

    return 0;
}