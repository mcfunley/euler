#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include "totient.h"
#include "factorize.h"


int prime_factor_totient(prime_factor* f) {
    int k = pow(f->mantissa, f->exponent-1);
    int x = k*(f->mantissa) - k;
    //printf("   phi(%d ^ %d) = %d\n", f->mantissa, f->exponent, x);
    return x;
}


int totient(int n) {
    if(n <= 0) {
        printf("Bad value for totient: %d\n", n);
        exit(1);
    }
    if(n == 1) {
        return 1;
    }

    prime_factor_result* pf = prime_factors(n);
    
    int t = 1, i = 0;
    for(; i < pf->count; i++) {
        t *= prime_factor_totient(&pf->pfs[i]);
    }

    prime_factor_result_free(pf);
    return t;
}
