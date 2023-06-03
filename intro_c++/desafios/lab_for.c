#include <stdio.h>

int main(void) {
    int n;
    double investimentoInicial, jurosAnuais, aumento;
    printf("Insira a quantidade de anos que deseja ver o resultado: ");
    scanf("%i", &n);
    printf("Insira o valor investido inicialmente em reais.: R$: ");
    scanf("%lf", &investimentoInicial);
    printf("Insira a taxa anual de juros em decimal (ex: 0.05 = 5%%): ");
    scanf("%lf", &jurosAnuais);
    
    aumento = 1;
    for(int i = 0; i < n; i++) {
        aumento *= (1 + jurosAnuais);
    }
    printf("%lf\n", aumento * investimentoInicial);
}