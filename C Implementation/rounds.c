#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 1024
#define NUM_ROWS 1000

int lam = 139;

void get_column(int column_num, char* file_name, int* output) {
    char buffer[BUFFER_SIZE];
    char command[BUFFER_SIZE];
    sprintf(command, "awk '{print $%d}' %s", column_num, file_name);
    FILE* fp = popen(command, "r");
    int i = 0;
    while (fgets(buffer, BUFFER_SIZE, fp)) {
        output[i] = atoi(buffer);
        i++;
    }
    pclose(fp);
}

void hash_first_set(int column_num, int* a_hash, int* b_hash, int* c_hash) {
    int A_col[NUM_ROWS], B_col[NUM_ROWS], C_col[NUM_ROWS];
    get_column(column_num, "A.txt", A_col);
    get_column(column_num, "B.txt", B_col);
    get_column(column_num, "C.txt", C_col);
    memset(a_hash, 0, NUM_ROWS * sizeof(int));
    memset(b_hash, 0, NUM_ROWS * sizeof(int));
    memset(c_hash, 0, NUM_ROWS * sizeof(int));
    int counterA = 0, counterB = 0, counterC = 0;
    for (int i = 0; i < NUM_ROWS; i++) {
        int value = A_col[i];
        if (a_hash[value] == 0) {
            char str[BUFFER_SIZE];
            sprintf(str, "%d", counterA);
            strcat(a_hash[value], str);
            counterA++;
        } else {
            strcat(a_hash[value], ",");
            char str[BUFFER_SIZE];
            sprintf(str, "%d", counterA);
            strcat(a_hash[value], str);
            counterA++;
        }
    }
    for (int i = 0; i < NUM_ROWS; i++) {
        int value = B_col[i];
        if (b_hash[value] == 0) {
            char str[BUFFER_SIZE];
            sprintf(str, "%d", counterB);
            strcat(b_hash[value], str);
            counterB++;
        } else {
            strcat(b_hash[value], ",");
            char str[BUFFER_SIZE];
            sprintf(str, "%d", counterB);
            strcat(b_hash[value], str);
            counterB++;
        }
    }
    for (int i = 0; i < NUM_ROWS; i++) {
        int value = C_col[i];
        if (c_hash[value] == 0) {
            char str[BUFFER_SIZE];
            sprintf(str, "%d", counterC);
            strcat(c_hash[value], str);
            counterC++;
        } else {
            strcat(c_hash[value], ",");
            char str[BUFFER_SIZE];
            sprintf(str, "%d", counterC);
            strcat(c_hash[value], str);
            counterC++;
        }
    }
}

unsigned int hash_with_constraints(const char *str, const unsigned int len, const unsigned int max, const unsigned int min, const unsigned int seed) {
    unsigned int hash = seed;
    unsigned int i;
    for (i = 0; i < len; i++) {
        hash = hash * 31 + str[i];
    }
    if (hash > max || hash < min) {
        hash = (hash % (max - min + 1)) + min;
    }
    return hash;
}

int main() {
    const char *str = "hello world";
    const unsigned int len = strlen(str);
    const unsigned int seed = 12345;
    const unsigned int max = 100;
    const unsigned int min = 1;
    unsigned int hash = hash_with_constraints(str, len, max, min, seed);
    printf("Hash of \"%s\" with constraints [%d, %d] is %u\n", str, min, max, hash);
    return 0;
}