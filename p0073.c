/*
Consider the fraction, n/d, where n and d are positive integers. If n<d and 
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of 
size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d <= 12,000?
 */
#include <stdio.h>
#include "euler.h"

int dmax = 12000;

int main() {
    //dmax = 8;
    int count = 0;
    for(int d = 2; d <= dmax; d++) {
        int min = (int)ceil(1.0 / 3.0 * d);
        if(!min) continue;

        int max = (int)(1.0 / 2.0 * d);
        //printf("min = %d, max = %d, d = %d\n", min, max, d);
        
        for(int n = min; n <= max; n++) {
            if(gcd(d, n) == 1) {
                //printf("%d / %d\n", n, d);
                count++;
            }
        }

        if(d % 1000 == 0) printf("%d\t%d\n", d, count - 2);
    }
    // subtract 2 to account for 1/3 and 1/2
    printf("%d\n", count - 2);
}
