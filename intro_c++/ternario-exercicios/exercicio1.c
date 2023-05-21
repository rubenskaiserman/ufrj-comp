#include <stdio.h>

int main(void) {
    double valorMensal = 7;
    double aguaConsumida = 0;

    printf("Insira o valor da água consumida em m³: ");
    scanf("%lf", &aguaConsumida);

    valorMensal += aguaConsumida > 100 ? 5 * (aguaConsumida - 100) : 0;
    aguaConsumida = aguaConsumida > 100 ? 100 : aguaConsumida;
    valorMensal += aguaConsumida > 30 ? 2 * (aguaConsumida - 30) : 0;
    aguaConsumida = aguaConsumida > 30 ? 30 : aguaConsumida;
    valorMensal += aguaConsumida > 10 ? aguaConsumida - 10 : 0;

    printf("Valor consumido: %lf\n", valorMensal);
}