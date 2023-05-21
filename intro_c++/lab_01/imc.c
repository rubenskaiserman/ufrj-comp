#include <stdio.h>

double imc(double m, double h);

int main(void) {
    double m, h;
    printf("Altura: ");
    scanf("%lf", &h);
    printf("Peso: ");
    scanf("%lf", &m);

    double imcResult = imc(m, h);
    printf("IMC: %.2lf\n", imcResult);

    return 0;
}

double imc(double m, double h) {
    return m / (h * h);
}