#include<stdio.h>
#include<math.h>

int main(void) {
    double a;
    double b;
    double c;

    printf("Informe o valor do cateto a: ");
    scanf("%le", &a);
    printf("Informe o valor do cateto b: ");
    scanf("%le", &b);

    c = sqrt(a * a + b * b);

    printf("O valor da hipotenusa eh: %f\n", c);

    return 0;
}