#include <stdio.h>
#define PI 3.14159 // Define uma constante PI
int main() {
    float raio, perimetro;
    printf("Informe o raio da circunferencia: ");
    scanf("%f", &raio);
    perimetro = 2 * PI * raio;
    printf("O perimetro da circunferencia de raio %.2f eh %.2f\n", raio, perimetro);
    return 0;
}