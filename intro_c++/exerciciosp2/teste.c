#include <stdio.h>
#include <stdlib.h>

int main(void) {
    FILE *file = fopen("./querover.txt", "w");

    fprintf(file, "FUNCIONO");

    fclose(file);
}