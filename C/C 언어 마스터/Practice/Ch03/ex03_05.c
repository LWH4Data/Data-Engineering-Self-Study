#include <stdio.h>

int main()
{   
    // float과 double을 구분하기 위해 뒤에 f를 붙인다.
    float floatValue1 = 3.14f;
    float floatValue2 = 2.718f;
    float sumFloat = floatValue1 + floatValue2;
    float productFloat = floatValue1 * floatValue2;

    printf("Sum (Float): %f\n", sumFloat);
    printf("Product (Float): %f\n", productFloat);

    double doubleValue1 = 123.456;
    double doubleValue2 = 789.012;
    double sumDouble = doubleValue1 + doubleValue2;
    double productDouble = doubleValue1 * doubleValue2;

    printf("Sum (Double): %f\n", sumDouble);
    printf("Product (Double): %f\n", productDouble);

    return 0;
}