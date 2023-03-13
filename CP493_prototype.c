#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char a_hash[10][100000] = {0};
char b_hash[10][100000] = {0};
char c_hash[10][100000] = {0};
int arr_4[100][3] = {0};
int completed_val[100] = {0};

int lam = 139 % 10;

int main() {
    int i, j;
    int outputA[100], outputB[100], outputC[100];
    int counterA = 0, counterB = 0, counterC = 0;
    char column_num[3] = "1";
    char commandA[100], commandB[100], commandC[100];
    char buffer[100];

    sprintf(commandA, "awk '{print $%s}' A.txt", column_num);
    sprintf(commandB, "awk '{print $%s}' B.txt", column_num);
    sprintf(commandC, "awk '{print $%s}' C.txt", column_num);

    // FILE *fp;
    // fp = popen(commandA, "r");
    // while (fgets(buffer, sizeof(buffer), fp) != NULL) {
    //     outputA[counterA++] = atoi(buffer);
    // }
    // pclose(fp);

    // fp = popen(commandB, "r");
    // counterB = 0;
    // while (fgets(buffer, sizeof(buffer), fp) != NULL) {
    //     outputB[counterB++] = atoi(buffer);
    // }
    // pclose(fp);

    // fp = popen(commandC, "r");
    // counterC = 0;
    // while (fgets(buffer, sizeof(buffer), fp) != NULL) {
    //     outputC[counterC++] = atoi(buffer);
    // }
    // pclose(fp);

    // for (i = 0; i < counterA; i++) {
    //     int value = outputA[i];
    //     if (i != counterA - 1) {
    //         sprintf(a_hash[value], "%s%d,", a_hash[value], i);
    //     } else {
    //         sprintf(a_hash[value], "%s%d", a_hash[value], i);
    //     }
    // }

    // for (i = 0; i < counterB; i++) {
    //     int value = outputB[i];
    //     if (i != counterB - 1) {
    //         sprintf(b_hash[value], "%s%d,", b_hash[value], i);
    //     } else {
    //         sprintf(b_hash[value], "%s%d", b_hash[value], i);
    //     }
    // }

    // for (i = 0; i < counterC; i++) {
    //     int value = outputC[i];
    //     if (i != counterC - 1) {
    //         sprintf(c_hash[value], "%s%d,", c_hash[value], i);
    //     } else {
    //         sprintf(c_hash[value], "%s%d", c_hash[value], i);
    //     }
    // }

    // for (i = 0; i < 10; i++) {
    //     if (completed_val[outputA[i]]) {
    //         continue;
    //     }

    //     for (j = 0; j < 10; j++) {
    //         int b_val = (10 + lam - i - j) % 10;
    //         if (strlen(b_hash[b_val]) > 0) {
    //             arr_4[i][0] = i;
    //             arr_4[i][1] = b_val;
    //             arr_4[i][2] = j;
    //             break;
    //         }
    //     }

    //     completed_val[outputA[i]] = 1;
    //     if (i == 9) {
    //         break;
    //     }
    // }

    return 0;
}