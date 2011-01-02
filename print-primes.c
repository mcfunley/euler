#include <stdio.h>
#include "primesdb.h"



int main() {
    primesdb* db = primesdb_init();
    prime_iter it;
    prime_iter_init(&it, db);

    int p = -1;
    while((p = prime_iter_next(&it)) > 0) {
        printf("%d\n", p);
    }

    primesdb_free(db);
    return 0;
}
