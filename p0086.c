#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int int_shortest_path(unsigned long a, unsigned long b, unsigned long c) {
    unsigned long s1 = (a + b) * (a + b) + c * c;
    unsigned long s2 = (a + c) * (a + c) + b * b;
    unsigned long s3 = (b + c) * (b + c) + a * a;
    unsigned long min = (
        (s1 < s2) ? ((s1 < s3) ? s1 : s3) : ((s2 < s3) ? s2 : s3)
    );

    double sp = sqrt(min);
    if((double)(int)sp == sp) {
        return 1;
    }
    return 0;
}


int main() {
    // answer is between 1000 and 2000, binary search by hand
    const unsigned long low = 1817, high = 1819;
    const unsigned long M = low + (high - low) / 2;

    int solutions = 0;
    for(int m = 1; m <= M; m++) {
        if(m % 100 == 0) {
            printf("m=%d ", m);
            fflush(stdout);
        }
        
        for(int n = m; n <= M; n++) {
            for(int p = n; p <= M; p++) {
                if(int_shortest_path(m, n, p)) {
                    solutions++;
                }
            }
        }
    }

    printf("\nSolutions for M=%lu: %d\n", M, solutions);
    return 0;
}
