#include <stdio.h>

int main(void) {
    double salario;
    printf("Insira seu salário: ");
    scanf("%lf", &salario);
    
    double newSalario = salario * 1.09;

    if(salario <= 3500) {
        newSalario += 200;
    }

    printf("Novo salário: %lf\n", newSalario);

    return 0;
}