#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * concat(char * s1, char * s2, char * s3) {
    size_t len1 = strlen(s1);
    size_t len2 = strlen(s2);
    size_t len3 = strlen(s3);
    char * result = malloc(len1 + len2 + len3 + 1);
    if (result == NULL) {
        fprintf(stderr, "Error: memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    memcpy(result, s1, len1);
    memcpy(result + len1, s2, len2);
    memcpy(result + len1 + len2, s3, len3);
    result[len1 + len2 + len3] = '\0';
    return result;
}

int * get_coloumn(char coloumn) {
    char commandA[50], commandB[50], commandC[50];
    char column_num[2];
    sprintf(column_num, "%c", coloumn);
    sprintf(commandA, "awk '{print $%c}' A.txt", coloumn);
    sprintf(commandB, "awk '{print $%c}' B.txt", coloumn);
    sprintf(commandC, "awk '{print $%c}' C.txt", coloumn);
    FILE * fpA = popen(commandA, "r");
    FILE * fpB = popen(commandB, "r");
    FILE * fpC = popen(commandC, "r");
    if (fpA == NULL || fpB == NULL || fpC == NULL) {
        fprintf(stderr, "Error: popen() failed\n");
        exit(EXIT_FAILURE);
    }
    char * line = NULL;
    size_t len = 0;
    size_t read;
    int indexA = 0, indexB = 0, indexC = 0;
    int * outputA = (int*)malloc(sizeof(int));
    int * outputB = (int*)malloc(sizeof(int));
    int * outputC = (int*)malloc(sizeof(int));
    if (outputA == NULL || outputB == NULL || outputC == NULL) {
        fprintf(stderr, "Error: memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    while ((read = getline(&line, &len, fpA)) != -1) {
        outputA = (int*)realloc(outputA, (indexA + 1) * sizeof(int));
        if (outputA == NULL) {
            fprintf(stderr, "Error: memory allocation failed\n");
            exit(EXIT_FAILURE);
        }
        outputA[indexA] = atoi(line);
        indexA++;
    }
    while ((read = getline(&line, &len, fpB)) != -1) {
        outputB = (int*)realloc(outputB, (indexB + 1) * sizeof(int));
        if (outputB == NULL) {
            fprintf(stderr, "Error: memory allocation failed\n");
            exit(EXIT_FAILURE);
        }
        outputB[indexB] = atoi(line);
        indexB++;
    }
    while ((read = getline(&line, &len, fpC)) != -1) {
        outputC = (int*)realloc(outputC, (indexC + 1) * sizeof(int));
        if (outputC == NULL) {
            fprintf(stderr, "Error: memory allocation failed\n");
            exit(EXIT_FAILURE);
        }
        outputC[indexC] = atoi(line);
        indexC++;
    }
    free(line);
    pclose(fpA);
    pclose(fpB);
    pclose(fpC);
   
}

int main() {
    FILE *fpC;
    char *line = NULL;
    size_t len = 0;
    size_t read;

    fpC = fopen("sample.txt", "r");
    if (fpC == NULL) {
        printf("Failed to open file\n");
        exit(EXIT_FAILURE);
    }

    while ((read = getline(&line, &len, fpC)) != -1) {
        // Process the line read from the file
        printf("Retrieved line of length %zu:\n", read);
        printf("%s", line);
    }

    // Free memory allocated for line
    free(line);

    // Close file
    fclose(fpC);

    // Rest of the code
    printf("File reading complete.\n");

    return 0;
}