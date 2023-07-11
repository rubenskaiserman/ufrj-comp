#include <stdio.h>
#include <stdlib.h>


void troca(int* i, int* j) {
    int *temp;
    temp = i;
    *i = *j;
    *j = temp;
}

int main()
{
    int x, *p;
    x = 100;
    p = malloc(sizeof(int));
    *p = x;

    printf("Valor de p: %d.\n", *p);

    free(p);
    int *i;
    int *j;
    i = malloc(2 * sizeof(int));
    j = malloc(2 * sizeof(int));
    i[0] = 29;
    i[1] = 261;
    j[0] = 532;
    j[1] = 111;
    troca(i, j);
    printf("i: %i, %i\n", i[0], i[1]);
    printf("j: %d, %d\n", j[0], j[1]);

    free(i);
    free(j);

    return 0;
}
