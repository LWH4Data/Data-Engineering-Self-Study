#include <stdio.h>

int main()
{
    int a;
    char b;
    float c;

    printf("정수를 입력하세요: ");
    scanf("%d", &a);

    printf("문자를 입력하세요: ");
    scanf(" %c", &b);

    printf("실수를 입력하세요: ");
    scanf("%f", &c);

    printf("입력받은 정수: %d\n", a);
    printf("입력받은 문자: %c\n", b);
    printf("입력받은 실수: %f\n", c);
}