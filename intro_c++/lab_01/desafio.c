#include <stdio.h>

int main(void) {
    double rendaMensal, imposto, valorTaxado;

    printf("Insira sua renda mensal: ");
    scanf("%lf", &rendaMensal);

    valorTaxado = rendaMensal - 1903.98;

    if(valorTaxado <= 922.67) {
        imposto = valorTaxado * 0.075;
    } else {
        imposto = 922.67 * 0.075;
        valorTaxado -= 922.67;
        
        if(valorTaxado <= 924.40) {
            imposto += valorTaxado * 0.15;
        } else {
            imposto += 924.40 * 0.15;
            valorTaxado -= 924.40;

            if (valorTaxado <= 913.63) {
                imposto += valorTaxado * 0.225;
            } else {
                imposto += 913.63 * 0.225;
                valorTaxado -= 913.63;
                
                imposto += valorTaxado * 0.275;
            }
        }
    }

    printf("Seu imposto a ser pago é %.2lf\n", imposto);
    printf("Sua alíquota é %.2lf%%\n", (imposto / rendaMensal)*100);
}