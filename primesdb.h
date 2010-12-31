#include <stdio.h>


typedef struct _prime_entry {
    int next;
    int prev;
} prime_entry;


typedef struct _primes_database {
    int max;
} primesdb;



void primesdb_init(primesdb* db);
