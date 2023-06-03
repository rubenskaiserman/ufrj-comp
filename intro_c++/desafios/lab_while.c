#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isPrimeNumber(int number) {
    for(int i = 2; i <= sqrt(number); i++) {
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
    int i = 2;
    while(i < number){
        if(isPrimeNumber(i)) {
            product += i;
        }
        i++;
    }
    printf("Product: %i\n", product);
}