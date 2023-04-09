#include <stdio.h>

int main() {
    int idade; // declara a variável idade

    printf("Digite sua idade: "); // imprime uma mensagem para o usuário
    scanf("%d", &idade); // lê um valor digitado e armazena na variável idade
    printf("Sua idade é %d anos.\n", idade); // imprime a idade digitada
    // note que %d é substituído pelo valor da variável idade

    return 0; // retorna 0 para indicar que o programa foi executado com sucesso
}