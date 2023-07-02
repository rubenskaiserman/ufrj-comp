#include <stdio.h>
#include <stdlib.h>

int * twoSum(int array[9], int n, int target) {
    int *result = malloc(sizeof(int) * 2);
    for(int i = 0; i < n - 1; i++) {
        if(array[i] + array[i + 1] == target) {
            result[0] = array[i];
            result[1] = array[i + 1];
            return result;
        }
    }
    return NULL;
}

int main(void) {
    int array[] = {1, 12, 3, 4, 5, 6, 7, 8, 9};
    int target = 13;

    int *result = NULL;
    result = twoSum(array, 9, target);
    printf("Par encontrado: %d + %d\n", result[0], result[1]);
    free(result);
}