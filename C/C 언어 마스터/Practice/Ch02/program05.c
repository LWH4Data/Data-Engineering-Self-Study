#include <stdio.h>

int main()
{   
    float x;

    printf("실수를 입력하세요: ");
    scanf("%f", &x);

    printf("입력한 숫자의 제곱은: %.2f입니다.", x * x);

    return 0;
}