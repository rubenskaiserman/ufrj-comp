#include <stdio.h>

// Leia a distância em Km e a quantidade de litros de gasolina consumidos por um
// carro em um percurso, calcule o consumo em Km/l e escreva uma mensagem de
// acordo com a tabela abaixo:

// CONSUMO (Km/l) MENSAGEM
// menor que 8 "Venda o carro!"
// entre 8 e 14 "Econômico"
// maior que 14 "Super econômico"

int main(void) {
    float distancia, litros, consumo;
    printf("Insira a distância percorrida em Km: ");
    scanf("%f", &distancia);
    printf("Insira a quantidade de litros consumidos: ");
    scanf("%f", &litros);
    consumo = distancia / litros;

    if (consumo < 8) {
        printf("Venda o carro!\n");
    } else if (consumo >= 8 && consumo <= 14) {
        printf("Econômico\n");
    } else {
        printf("Super econômico\n");
    }

    return 0;
}