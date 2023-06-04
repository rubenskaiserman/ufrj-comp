#include <stdio.h>
#include <stdlib.h>

int comb(int n, int k) {
    printf("Recursão n, k: %d %d\n", n, k);
    if(k == 1) {
        return n;
    } else if( k == n) {
        return 1;
    } 
    return comb(n - 1, k - 1) + comb(n - 1, k);
}

long factorial(int n) {
    long factorial = 1; 
    for(int i = 2; i <= n; i++) {
        factorial *= i;
    }
    return factorial;
}

long combNotRecursive(int n, int k) {
    return factorial(n)/(factorial(k) * factorial(n - k));
}

int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int k = atoi(argv[2]);

    printf("comb: %d\n", comb(n, k));
    printf("Without recursion: %ld\n", combNotRecursive(n, k));
}