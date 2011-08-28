#include <stdio.h>
#include <stdlib.h>
#include "primesdb.h"

/*
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be
prime. For example, taking 7 and 109, both 7109 and 1097 are
prime. The sum of these four primes, 792, represents the lowest sum
for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
 */

int cat_test(int p, int q) {
    char s1[255], s2[255];
    snprintf(s1, 255, "%d%d", p, q);
    snprintf(s2, 255, "%d%d", q, p);
    if(primesdb_is_prime(atoi(s1)) && primesdb_is_prime(atoi(s2))) {
        return 1;
    }
    return 0;
}


int main() {
    int pairs[1000][150];
    prime_iter f, p;
    prime_iter_init(&f);
    
    int i = 0;
    for(; i < 1000; i++) {
        prime_iter_init(&p);

        pairs[i][0] = prime_iter_next(&f);
        
        int j = 0;
        while((j = prime_iter_next(&p)) <= pairs[i][0]);
        
        int c = 1;
        while(c < 150 && (j = prime_iter_next(&p)) < 50000) {
            if(cat_test(j, pairs[i][0])) {
                pairs[i][c] = j;
                c++;
            }
        }

        //printf("%d %d %d %d\n", pairs[i][0], pairs[i][1], pairs[i][2], pairs[i][3]);
    }

    for(i = 0; i < 1000; i++) {
        int p0 = pairs[i][0];
        int k = 1;
        for(; k < 150; k++) {
            int pk = pairs[i][k];
            if(pk == 0) break;
            if(k == i) continue;

            int l = k+1;
            for(; l < 150; l++) {
                int pl = pairs[i][l];
                if(pl == 0) break;
                if(!cat_test(pk, pl)) continue;

                int m = l+1;
                for(; m < 150; m++) {
                    int pm = pairs[i][m];
                    if(pm == 0) break;
                    if(!cat_test(pm, pk)) continue;
                    if(!cat_test(pm, pl)) continue;

                    int n = m+1;
                    for(; n < 150; n++) {
                        int pn = pairs[i][n];
                        if(pairs[i][n] == 0) break;
                        if(!cat_test(pn, pk)) continue;
                        if(!cat_test(pn, pl)) continue;
                        if(!cat_test(pn, pm)) continue;

                        int s = p0 + pk + pl + pm + pn;
                        printf("%d: %d %d %d %d %d\n", s, p0, pk, pl, pm, pn);
                        fflush(stdout);
                    }
                }
            }
        }
    }

    return 0;
}
