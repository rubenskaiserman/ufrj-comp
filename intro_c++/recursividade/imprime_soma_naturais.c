#include <stdio.h>

int some(int number) {
    if(number == 1 || number == 0) {
        return number;
    }
    return some(number - 1) + number;
}

int main(void) {
    int soma = some(7);
    printf("%d\n", soma);
}

