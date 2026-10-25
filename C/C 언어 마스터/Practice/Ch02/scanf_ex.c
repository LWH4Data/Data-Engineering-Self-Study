#pragma warning(disable: 4996)
#include <stdio.h>

int main()
{
    double num;
    
    printf("원의 반지름을 입력하세요: ");
    scanf("%lf", &num);
    
    printf("원의 면적 %.2lf\n", 3.14 * num * num);
    printf("원의 둘레 %.2lf", 2 * 3.14 * num);

    return 0;
}