#include <stdio.h>

int main(void) {
    int n;
    printf("Insira um número: ");
    scanf("%d", &n);

    if (n % 2 == 0) {
        printf("O número %d é par", n);
        if( n % 4 == 0) {
            printf(" e múltiplo de 4");
        }
        printf("\n");
    } else {
        printf("O número %d é ímpar\n", n);
    }

    return 0;
}