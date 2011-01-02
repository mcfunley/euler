#include <stdio.h>


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


primesdb* primesdb_init(void);
void primesdb_free(primesdb* db);

void prime_iter_init(prime_iter* it, primesdb* db);
int prime_iter_next(prime_iter* it);

int primesdb_is_prime(primesdb* db, int i);
