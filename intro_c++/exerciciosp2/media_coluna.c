#include <stdio.h>
#include <stdlib.h>

double mediaColuna(int **matrix, int column, int height)
{
    double media = 0;
    for (int i = 0; i < height; i++)
    {
        printf("%d\n", matrix[i][column - 1]);
        media += matrix[i][column - 1];
    }

    return (media / height);
}

int main(void)
{
    int **matrix;
    matrix = (int **) malloc(7 * sizeof(int *));

    int k = 0;
    for (int i = 0; i < 7; i++)
    {
        matrix[i] = (int *) malloc(9 * sizeof(int));
        for (int j = 0; j < 9; j++)
        {
            matrix[i][j] = k;
            k++;
        }
    }

    double media = mediaColuna(matrix, 1, 7);

    for (int i = 0; i < 7; i++)
    {
        free(matrix[i]);
    }
    free(matrix);

    printf("media: %lf\n", media);
}