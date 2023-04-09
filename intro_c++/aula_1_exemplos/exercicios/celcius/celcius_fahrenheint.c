#include <stdio.h>

int main(void) {
    double celsius;
    double fahrenheit;

    printf("Informe a temperatura em Fahrenheit: ");
    scanf("%le", &fahrenheit);

    celsius = (fahrenheit - 32) * 5 / 9;
    printf("A temperatura em celsius eh: %f\n", celsius);

    return 0;
}