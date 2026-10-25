#include <stdio.h>

int main()
{
    char ch;
    char str[10];
    int i;
    float f;

    printf("문자를 입력하세요: ");
    scanf("%c", &ch);

    printf("문자열을 입력하세요: ");
    scanf("%s", str);

    printf("입력받은 문자: %c\n", ch);
    printf("입력받은 문자열: %s\n", str);

    printf("정수를 입력하세요: ");
    scanf("%d", &i);

    printf("실수를 입력하세요: ");
    scanf("%f", &f);

    printf("입력받은 정수: %d\n", i);
    printf("입력받은 실수: %f\n", f);

    return 0;
}