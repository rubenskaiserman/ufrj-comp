#include <stdio.h>

int main(void) {
    int a = 1;
    int b = 0;
    int c = 0;
    int n = 0;
    printf("Insira a quantidade de termos: ");
    scanf("%d", &n);

    int i = 0;
    while (i < n) {
        printf("%d ", a + b);
        c = a;
        a = b;
        b = a + c;
        
        i++;
    }
    printf("\n");

    return 0;
}
