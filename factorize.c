#include <stdlib.h>
#include "factorize.h"
#include "vector.h"
#include "primesdb.h"

void prime_factor_result_free(prime_factor_result* r) {
    free(r->pfs);
    free(r);
}


ivector* get_prime_factor_vector(int n) {
    ivector* factors = ivector_init();
    prime_iter it;
    prime_iter_init(&it);

    int p = prime_iter_next(&it);
    while(p <= n) {
        if(n % p == 0) {
            n /= p;
            ivector_append(factors, p);
        } else {
            p = prime_iter_next(&it);
        }
    }

    return factors;
}



prime_factor_result* prime_factor_result_init(ivector* primes) {
    int max = ivector_count(primes);
    prime_factor_result* r = (prime_factor_result*)
        malloc(sizeof(prime_factor_result));
    if(!r) {
        perror("malloc error - prime_factor_result");
        exit(1);
    }

    r->pfs = (prime_factor*)malloc(sizeof(prime_factor) * max);
    if(!(r->pfs)) {
        perror("malloc error - prime_factor*");
        exit(1);
    }
    r->count = 0;
    return r;
}


prime_factor_result* simple_result(int m, int e) {
    prime_factor_result* r = (prime_factor_result*)
        malloc(sizeof(prime_factor_result));
    r->pfs = (prime_factor*)malloc(sizeof(prime_factor));
    r->count = 1;
    r->pfs[0].exponent = e;
    r->pfs[0].mantissa = m;
    return r;
}


prime_factor_result* prime_factors(int n) {
    if(n == 1) {
        return simple_result(1, 1);
    }

    ivector* primes = get_prime_factor_vector(n);
    ivector_iter* iter = ivector_iter_init(primes);

    prime_factor_result* r = prime_factor_result_init(primes);
    int i = -1;
    int last = -1;
    while(ivector_iter_more(iter)) {
        int p = ivector_iter_next(iter);
        if(p == last) {
            r->pfs[i].exponent++;
        } else {
            i++;
            r->pfs[i].mantissa = p;
            r->pfs[i].exponent = 1;
            last = p;
        }
    }
    
    r->count = i+1;

    ivector_free(primes);
    ivector_iter_free(iter);

    return r;
}

