#include <stdio.h>
#include <stdlib.h>

int power(int n, int potencia) {
    if(potencia == 0) {
        return 1;
    } 
    else if (potencia == 1) {
        return n;
    }
    return n * power(n, potencia - 1);
}

int main(int argc, char *argv[]) {
    int number = atoi(argv[1]);
    int potencia = atoi(argv[2]);
    printf("Resultado: %d\n", power(number, potencia)); 
}