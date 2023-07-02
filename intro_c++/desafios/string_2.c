#include <stdio.h>
#include <string.h>

void substituirPalavra(char frase[], char palavaraAlvo[], char palavraNova[]) {
    int sentenceLength = strlen(frase);
    int targetWordLength = strlen(palavaraAlvo);
    int newWordLength = strlen(palavraNova);
    int word_offset = 0;
    char newSentence[400];

    for(int i = 0; i < sentenceLength; i++) {
        int match = 0;
        for(int j = 0; j < targetWordLength; j++) {
            if(frase[i + j] == palavaraAlvo[j]) {
                match++;
            } else {
                match = 0;
                break;
            }
        }
        if(match == targetWordLength) {
            for(int k = 0; k < newWordLength; k++) {
                newSentence[i + word_offset + k] = palavraNova[k];
            }
            word_offset += newWordLength - targetWordLength;
            i += targetWordLength - 1;
        }
        else {
            printf("%c\n", frase[i]);
            newSentence[i + word_offset] = frase[i];
        }
    }
    int i = 0;
    while (newSentence[i] != '\0') {
        printf("%c", newSentence[i]);
        i++;
    }
    printf("\n");
}

int main() {
    substituirPalavra("O gato é preto e o cachorro é preto também", "batatinha", "branco");
}