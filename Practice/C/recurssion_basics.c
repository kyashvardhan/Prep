void printNumbers(int n) {
    if (n == 0) return;        // base case
    printNumbers(n - 1);       // smaller problem
    printf("%d ", n);          // print after call
}

// Factorial

int fact(int n) {
    if (n == 0) return 1;
    return n * fact(n - 1);
}
