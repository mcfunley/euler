#ifndef FACTORIZE_H
#define FACTORIZE_H


typedef struct {
    int mantissa;
    int exponent;
} prime_factor;


typedef struct {
    prime_factor* pfs;
    int count;
} prime_factor_result;


prime_factor_result* prime_factors(int n);
void prime_factor_result_free(prime_factor_result* r);

#endif
