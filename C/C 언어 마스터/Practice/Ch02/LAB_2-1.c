#include <stdio.h>

int main()
{
    printf("### 형식 지정자 적용 ###\n");
    printf("12345678901234567890\n");
    printf("%10c\n", 'A');
    printf("%10d\n", 128);
    printf("%10f\n", 3.141592);
    printf("%10.3f\n", 3.141592);
    printf("%10s\n", "Love");
}