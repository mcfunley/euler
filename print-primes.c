#include <stdio.h>
#include "primesdb.h"



int main() {
    prime_iter it;
    prime_iter_init(&it);

    int p = -1;
    while((p = prime_iter_next(&it)) > 0) {
        printf("%d\n", p);
    }

    return 0;
}
