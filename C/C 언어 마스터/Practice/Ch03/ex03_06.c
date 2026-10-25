#include <stdio.h>

int main()
{
    float base = 5.0;
    float height = 3.0;
    float triangleArea = (base * height) / 2.0;

    printf("삼각형 넓이: %.2f\n", triangleArea);

    double width = 4.0;
    double rheight = 6.0;
    double rectangleArea = width * rheight;

    printf("사각형의 넓이: %.2lf\n", rectangleArea);

    return 0;
}