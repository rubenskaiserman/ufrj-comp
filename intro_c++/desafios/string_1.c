#include <stdio.h>
#include <string.h>

#define MAX_WORDS 400
#define MAX_WORD_LENGTH 50

int main() {
    char input[1000];
    char words[MAX_WORDS][MAX_WORD_LENGTH];
    int frequencies[MAX_WORDS] = {0};
    int numWords = 0;

    printf("Digite uma frase: ");
    fgets(input, sizeof(input), stdin);

    char word[MAX_WORD_LENGTH];
    int wordIndex = 0;
    for (int i = 0; i < strlen(input); i++) {
        if (input[i] == ' ' || input[i] == '\n') {
            if (wordIndex > 0) {
                word[wordIndex] = '\0';
                int found = 0;

                for (int j = 0; j < numWords; j++) {
                    if (strcmp(word, words[j]) == 0) {
                        frequencies[j]++;
                        found = 1;
                        break;
                    }
                }

                if (!found) {
                    strcpy(words[numWords], word);
                    frequencies[numWords] = 1;
                    numWords++;
                }

                wordIndex = 0;
            }
        } else {
            if (wordIndex < MAX_WORD_LENGTH - 1) {
                word[wordIndex] = input[i];
                wordIndex++;
            }
        }
    }

    printf("Frequência das palavras na frase:\n");
    for (int i = 0; i < numWords; i++) {
        printf("%s: %d\n", words[i], frequencies[i]);
    }

    return 0;
}
