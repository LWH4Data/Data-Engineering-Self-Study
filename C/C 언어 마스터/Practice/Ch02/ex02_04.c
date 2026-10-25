#include <stdio.h>

int main() 
{
    printf("%d %c %f\n", 10, 'z', 11.23);
    printf("%d\t %c\t %f\n", 10, 'z', 14.23);
    printf("슬램덩크 강백호는 %d 등번호\n", 10);
    printf("등번호 %6d\n", 10);
    printf("등번호 %-6d\n", 10);
    printf("강백호의 올해 필드 성공률이 %8.2f으로 오른 것으로 보인다.\n", 11.23);
    printf("강백호의 올해 자유투 성공률이 %08.2f으로 오른 것으로 보인다.\n", 14.23);

    return 0;
}