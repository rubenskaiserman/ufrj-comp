#include <stdio.h>

int main(void)
{
    int x, y, *p;
    y = 0;
    p = &y;
    x = *p;
    // x = 0
    x = 4;
    // x = 4
    (*p)++;
    // y = 1
    --x; 
    // x = 3
    (*p) += x;
    // y = 4

    printf("%d\n", x);
    printf("%d\n", y);
}