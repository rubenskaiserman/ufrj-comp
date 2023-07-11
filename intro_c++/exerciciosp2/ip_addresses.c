#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 100
#define OUTPUT_FILE_NAME "relatorio_ips.txt"

int isIPValid(char *ip) {
    int x, y1, y2, y3;
    int count = 0;

    char *token = ip;
    while (*token != '\0' && count < 4) {
        int num = 0;
        int multiplier = 1;

        while (*token != '.' && *token != '\0') {
            if (*token < '0' || *token > '9') {
                return 0; // Invalid character in IP
            }
            num = (num * 10) + (*token - '0');
            token++;
        }

        if (count == 0) {
            x = num;
        } else if (count == 1) {
            y1 = num;
        } else if (count == 2) {
            y2 = num;
        } else if (count == 3) {
            y3 = num;
        }

        if (*token == '.') {
            token++;
        }

        count++;
    }

    if (count != 4) {
        return 0; // Invalid IP format
    }

    if (x < 1 || x > 255) {
        return 0;
    }

    if (y1 < 0 || y1 > 255 || y2 < 0 || y2 > 255 || y3 < 0 || y3 > 255) {
        return 0;
    }

    return 1;
}

int main() {
    FILE *inputFile, *outputFile;
    char line[MAX_LINE_LENGTH];

    // Open the input file
    inputFile = fopen("teste.txt", "r");
    if (inputFile == NULL) {
        printf("Error opening the input file.\n");
        return 1;
    }

    // Open the output file
    outputFile = fopen(OUTPUT_FILE_NAME, "w");
    if (outputFile == NULL) {
        printf("Error opening the output file.\n");
        return 1;
    }

    // Read each line from the input file
    while (fgets(line, sizeof(line), inputFile)) {
        line[strcspn(line, "\n")] = '\0'; // Remove the newline character

        // Check if the IP address is valid
        if (isIPValid(line)) {
            fprintf(outputFile, "%s - Valid IP\n", line);
        } else {
            fprintf(outputFile, "%s - Invalid IP\n", line);
        }
    }

    // Close the files
    fclose(inputFile);
    fclose(outputFile);

    printf("Report generated successfully in the file %s.\n", OUTPUT_FILE_NAME);

    return 0;
}
