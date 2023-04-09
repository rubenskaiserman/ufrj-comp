#include <stdio.h>

int main(void) {
    double nota1;
    double nota2;
    double media;

    printf("Informe a primeira nota: ");
    scanf("%le", &nota1);
    printf("Informe a segunda nota: ");
    scanf("%le", &nota2);

    media = (nota1 + nota2) / 2;
    printf("Sua média é %le\n", media);

    return 0;
}