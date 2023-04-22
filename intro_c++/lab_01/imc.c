#include <stdio.h>

int main(void) {
    double imc, h;
    char sexo;
    
    printf("Informe seu sexo [M/F]: ");
    scanf("%c", &sexo);
    printf("Insira sua altura: ");
    scanf("%lf", &h);

    if (sexo == 'M') {
        imc = 72.7 * h - 58;
    } else if(sexo == 'F') {
        imc = 62.1 * h - 44.7;
    } else {
        printf("Sexo inválido!");
    }
    printf("Seu peso ideal é %lf\n", imc);

    return 0;
}