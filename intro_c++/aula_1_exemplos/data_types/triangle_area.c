#include <stdio.h>

int main(void) {
    double base;
    double height;

    printf("Insert the base of the triangle: ");
    scanf("%le", &base);
    printf("Insert the height of the triangle: ");
    scanf("%le", &height);

    double area = (base * height) / 2;
    printf("The area of the triangle is: %f\n", area);

    return 0;
}