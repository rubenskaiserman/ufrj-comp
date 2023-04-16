#include <stdio.h>

// Mf = {[(N1 + N2)/2]*0.8 + (T * 0.2)}

int main(void) {
    double N1, N2, Mf, T, Ps, Nf;
    printf("Insira a nota da primeira prova: ");
    scanf("%lf", &N1); 
    printf("Insira sua segunda nota: ");
    scanf("%lf", &N2);
    printf("Insira a nota do trabalho: ");
    scanf("%lf", &T);
    Mf = (((N1 + N2)/2)*0.8 + (T * 0.2));

    if(Mf >= 7){
        printf("Aluno aprovado\n");
        return 0;
    } else if(Mf >= 3) {
        printf("Insira a nota da prova final: ");
        scanf("%lf", &Ps);
        Nf = (Mf + Ps)/2;

        if (Nf >= 5) {
            printf("Aluno aprovado\n");
            return 0;
        }
    }
    printf("Aluno reprovado\n");
    return 0;
}