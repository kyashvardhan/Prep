void printNumbers(int n) {
    if (n == 0) return;        // base case
    printNumbers(n - 1);       // smaller problem
    printf("%d ", n);          // print after call
}
