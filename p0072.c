#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "primesdb.h"
#include "totient.h"

int dmax = 1000000;
int* primes;
int* prime_test;
int n_primes = 0;

int main() {
    // dmax = 8;
    // dmax = 10000;
    // http://en.wikipedia.org/wiki/Euler's_totient_function
    // we want: sum(phi(d) for all d)
    unsigned long count = 0;
    for (int d = 2; d <= dmax; d++) {
        count += totient(d);
        if(d % 10000 == 0) {
            printf("%d %lu\n", d, count);
        }
    }
    printf("%lu\n", count);
}

