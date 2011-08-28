#include "euler.h"


int main() {
    printf("     ");
    int i = 1;
    for(; i < 100; i++) {
        if(i % 10 == 0) {
            printf("\n");
        }
        printf("%5d", totient(i));
    }
    printf("\n");
    return 0;
}
