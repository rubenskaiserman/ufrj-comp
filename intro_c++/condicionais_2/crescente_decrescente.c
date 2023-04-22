#include <stdio.h>

int main(void) {
    double a, b, c, d;
    printf("Digite o primeiro número: ");
    scanf("%lf", &a);
    printf("Digite o segundo número: ");
    scanf("%lf", &b);
    printf("Digite o terceiro número: ");
    scanf("%lf", &c);
    printf("Digite o quarto número: ");
    scanf("%lf", &d);
    
    if (a < b && b < c && c < d) {
        printf("Crescente\n");
    } else if (a > b && b > c && c > d) {
        printf("Decrescente\n");
    } else {
        printf("Desordenado\n");
    }

    return 0;
}