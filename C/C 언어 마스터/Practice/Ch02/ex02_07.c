// 2개의 정수와 연산자를 입력받아 덧셈 결과를 출력하는 프로그램.
#include <stdio.h>

int main()
{
    int a, b;
    char op;

    printf("두 정수 덧셈 (ex 10 + 20): ");
    scanf("%d %c %d", &a, &op, &b);

    printf("%d %c %d = %d\n", a, op, b, a + b);

    return 0;
}