#include <stdio.h>

int main(void) {
    double a, b, c;
    printf("Insira o maior lado do triangulo: ");
    scanf("%lf", &a);
    printf("Insira o segundo lado do triangulo: ");
    scanf("%lf", &b);
    printf("Insira o terceiro lado do triangulo: ");
    scanf("%lf", &c);

    if(a > b + c) {
        printf("Não é um triangulo\n");
    } else if(a * a == b * b + c * c) {
        printf("Triangulo retângulo\n");
    } else if(a * a > b * b + c * c) {
        printf("Triangulo obtusângulo\n");
    } else if(a * a < b * b + c * c) {
        printf("Triangulo acutângulo\n");
    } 
}