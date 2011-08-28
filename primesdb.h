#include <stdio.h>

#ifndef PRIMESDB_H
#define PRIMESDB_H


typedef struct {
    int next;
    int prev;
} prime_entry;


typedef struct {
    int max;
    size_t sz;
    int filedesc;
} primesdb;

typedef struct { 
    int p;
    primesdb* db;
} prime_iter;

void primesdb_free(void);

void prime_iter_init(prime_iter* it);
int prime_iter_next(prime_iter* it);

int primesdb_is_prime(int i);


#endif
