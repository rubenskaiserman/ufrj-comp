#include <stdio.h>
#include <stdbool.h>

bool isPrimeNumber(int number) {
    for(int i = 2; i < number/i + 1; i++) {
        if(number % i == 0) {
            return false;
        }
    }
    return true;
}

int main(void) {
    int number;
    printf("Insira o número: ");
    scanf("%i", &number);
    int product = 0;
    for(int i = 2; i < number; i++){
        if(isPrimeNumber(i)) {
            product += i;
        }
    }
    printf("Product: %i\n", product);
}