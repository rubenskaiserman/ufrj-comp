#include <stdio.h>
#include <stdbool.h>

bool isPerfectNumber(int n);

int main(void) {
    printf("Número perfeito: %s\n", isPerfectNumber(8128) ? "true" : "false");
}

int addUpIfDivisible(int numerador, int denominador) {
    if(numerador % denominador == 0) {
        return denominador;
    }
    return 0;
}

bool isPerfectNumber(int n) {
    int totalSum = 0;
    for(int i = 1; i < n; i++) {
        totalSum += addUpIfDivisible(n, i);
    }
    if(totalSum == n) {
        return true;
    }
    return false;
}