#include <stdio.h>
#include <stdlib.h>
#include "euler.h"
#include <math.h>



int main() {
    int end = 10000000;
    int i = 2;
    float min = 0;
    int nmin = 0;
    for(; i < end; i++) {
        int t = totient(i);
        float r = ((float)i) / t;
        if((r < min || nmin == 0) && is_perm(t, i)) {
            min = r;
            nmin = i;
        }
        
        if(i % 1000 == 0) {
            float pct = ((float)i) / end * 100;
            printf("%20d %3.2f%%\r", i, pct);
            fflush(stdout);
        }
    }
    
    printf("\n%d\n", nmin);
    return 0;
}
