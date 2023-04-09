#include <stdio.h>

int main(void)
{
    char name[40];
    printf("Insert your name: ");
    scanf("%s", name);

    printf("Hello, %s\n", name);
    
    return 0;
}