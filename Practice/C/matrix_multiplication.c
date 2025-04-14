#include <stdio.h>

#define ROW1 2
#define COL1 3
#define ROW2 3
#define COL2 2

int main() {
    // Ensure COL1 == ROW2 for multiplication.
    int A[ROW1][COL1] = { {1, 2, 3}, {4, 5, 6} };
    int B[ROW2][COL2] = { {7, 8}, {9, 10}, {11, 12} };
    int C[ROW1][COL2] = {0};

    // Multiply matrices A and B, store result in C.
    for (int i = 0; i < ROW1; i++) {
        for (int j = 0; j < COL2; j++) {
            for (int k = 0; k < COL1; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    // Output the result.
    printf("Resultant Matrix:\n");
    for (int i = 0; i < ROW1; i++) {
        for (int j = 0; j < COL2; j++) {
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }

    return 0;
}
