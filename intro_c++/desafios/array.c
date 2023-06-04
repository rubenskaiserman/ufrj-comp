#include <stdio.h>


int printPrimeiroPar(int x, int array[], int length) {
    for(int i = 1; i < length; i++) {
        if(array[i] + array[i - 1] == x) {
            printf("Par encontrado: %d (índice %d) + %d (índice %d)\n", array[i - 1], i - 1, array[i], i);
            return 0;
        }
    }
    printf("Nenhum par consecutivo encontrado\n");
    return 0;
}

int main(void){
    int array[] = {2, 4, 7, 5, 9, 8};
    int x = 12;
    int length = 6;
    printPrimeiroPar(x, array, length);
}