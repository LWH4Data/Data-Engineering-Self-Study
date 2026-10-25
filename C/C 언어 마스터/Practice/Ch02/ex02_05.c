#include <stdio.h>

int main()
{
    int a = 1234;
    // 최소 너비 8칸 출력.
    printf("[%d]\n", a);      // 정수 출력
    printf("[%8d]\n", a);     // 오른쪽 정렬
    printf("[%-8d]\n", a);    // 왼쪽 정렬
    printf("[%+8d]\n", a);    // 오른쪽 정렬, 부호 표시
    printf("[%08d]\n", a);    // 공백 채움
    printf("[%+08d]\n", a);   // 부호 표시, 공백 채움

    char b = 'A';
    double c = 3.14159;

    printf("[%c]\n", b);      // 문자 출력
    printf("[%8c]\n", b);     // 오른쪽 정렬
    printf("[%-8c]\n", b);    // 왼쪽 정렬
    printf("[%f]\n", c);      // 소수점 아래 여섯 자리 실수 출력
    printf("[%8.3f]\n", c);   // 오른쪽 정렬, 소수점 아래 세 자리 출력
    printf("[%-8.3f]\n", c);  // 왼쪽 정렬, 소수점 아래 세 자리 출력
    printf("[%+8.3f]\n", c);  // 부호 표시, 소수점 아래 세 자리 출력
    printf("[%08.3f]\n", c);  // 공백 채움, 소수점 아래 세 자리 출력
    printf("[%+08.3f]\n", c); // 부호 표시, 공백 채움, 소수점 아래 세 자리 출력
}