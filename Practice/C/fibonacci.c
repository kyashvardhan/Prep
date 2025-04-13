#include <stdio.h>

// Function to print Fibonacci sequence up to n terms
void printFibonacci(int n) {
    long long a = 0, b = 1, next;
    printf("Fibonacci Sequence: ");
    for (int i = 0; i < n; i++) {
        printf("%lld ", a);
        next = a + b;
        a = b;
        b = next;
    }
    printf("\n");
}

int main() {
    int n;
    printf("Enter number of terms: ");
    scanf("%d", &n);
    if (n <= 0) {
        printf("Please enter a positive integer.\n");
        return 1;
    }
    printFibonacci(n);
    return 0;
}
