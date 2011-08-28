#include <stdio.h>
#include "ncurses.h"
#include "euler.h"


float ratio(int n) {
    return ((float)n) / totient(n);
}


int main() {
    float max = 0;
    int nmax = 0;
    int i = 1;
    int end = 1000000;
    for(; i < end+1; i++) {
        float r = ratio(i);
        if(r > max) {
            max = r;
            nmax = i;
        }
        
        float pct = ((float)i) / end;
        printf("%0.4f%%\r", pct);
        fflush(stdout);
    }

    printf("\n%d\n", nmax);
    return 0;
}
