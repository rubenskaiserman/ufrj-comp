#include <stdio.h>

int main(void) {
    int mes;
    printf("Insira um número entre 1 e 12: ");
    scanf("%d", &mes);

    switch (mes) {
        case 1:
            printf("Janeiro\n");
            break;
        case 2:
            printf("Fevereiro\n");
            break;
        case 3:
            printf("Março\n");
            break;
        case 4:
            printf("Abril\n");
            break;
        case 5:
            printf("Maio\n");
            break;
        case 6:
            printf("Junho\n");
            break;
        case 7:
            printf("Julho\n");
            break;
        case 8:
            printf("Agosto\n");
            break;
        case 9:
            printf("Setembro\n");
            break;
        case 10:
            printf("Outubro\n");
            break;
        case 11:
            printf("Novembro\n");
            break;
        case 12:
            printf("Dezembro\n");
            break;
        default:
            printf("Input inválido\n");
    }

    // Nota, uma abordagem alternativa sería à seguinte:
    // char meses[][20] = {"Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"};
    // int mes;
    // printf("Insira um número entre 1 e 12: ");
    // scanf("%d", &mes);
    // if(1 <= mes && mes <= 12) {
    //     printf("%s\n", meses[mes - 1]);
    // } else {
    //     printf("Input inválido");
    // }

    // A abordagem alternativa é interessante devido à uma simplificação e redução na quantidade de código necessária.

}