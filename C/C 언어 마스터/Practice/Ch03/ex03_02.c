#include <stdio.h>

int main()
{
    short sh = 12;
    int nt = 155;
    long long on = 1666;

    printf("자료형의 크기를 알아보는 코드 \n");
    printf("1. short : %dbyte, %dbyte \n", sizeof(sh), sizeof sh);
    printf("2. int : %dbyte, %dbyte \n", sizeof(nt), sizeof nt);
    printf("3. long long %dbyte, %dbyte \n", sizeof(on), sizeof on);

    return 0;
}