#include <stdio.h>
#include "euler.h"


float ratio(int n) {
    return ((float)n) / totient(n);
}


int main() {
    float max = 0;
    int nmax = 0;
    int i = 1;
    int end = 1000000;
    //int end = 100;

    for(; i < end+1; i++) {
        float r = ratio(i);
        if(r > max) {
            max = r;
            nmax = i;
        }

        if(i % 100 == 0) {
            float pct = ((float)i) / end * 100;
            printf("%0.4f%%\r", pct);
            fflush(stdout);
        }
    }

    printf("\n%d\n", nmax);
    return 0;
}
