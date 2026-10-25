#include <stdio.h>

int main()
{
    int total = 80;
    float average = 95.2f;

    printf("총점: %d\n", total);
    printf("평균: %.2f\n", average);  // 소수점 아래 두 자리까지만 출력
    printf("총점: %d, 평균: %.2f\n", total, average);

    return 0;
}