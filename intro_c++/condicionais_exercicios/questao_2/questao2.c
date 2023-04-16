#include <stdio.h>

int main(void) {
    int day, month, year;
    printf("Insira o dia de seu nascimento: ");
    scanf("%d", &day);
    printf("Insira seu mês de nascimento: ");
    scanf("%d", &month);
    printf("Insira seu ano de nascimento: ");
    scanf("%d", &year);

    int strangeSum = day * 100 + month + year;
    int strangeFirstBit = (int) strangeSum/100;
    int strangeSecondBit = strangeSum - strangeFirstBit * 100;

    int secondStrangeSum = strangeFirstBit + strangeSecondBit;
    int result = secondStrangeSum % 5;

    if(result == 0) {
        printf("Timido\n");
    } else if(result == 1) {
        printf("Sonhador\n");
    } else if(result == 2) {
        printf("Paquerador\n");
    } else if(result == 3) {
        printf("Atraente\n");
    } else {
        printf("Irresistível\n");
    }
    return 0;
}