#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include "primesdb.h"


#define PRIME_CHUNK_SIZE 4096*10

struct prime_chunk_el {
    int primes[PRIME_CHUNK_SIZE];
    struct prime_chunk_el* next;
};

typedef struct prime_chunk_el prime_chunk;


int read_primes(prime_chunk** out) {
    FILE* f = fopen("primes.txt", "r");
    if(!f) {
        fprintf(stderr, "Error opening primes.txt\n");
        exit(1);
    }

    // read the primes into dynamically allocated chunks. 
    prime_chunk* head = (prime_chunk*)malloc(sizeof(prime_chunk)), *c = head;
    int i = 0;
    int temp, last = -1;
    while(fscanf(f, "%d", &temp) != EOF) {
        if(i == PRIME_CHUNK_SIZE) {
            prime_chunk* c2 = (prime_chunk*)malloc(sizeof(prime_chunk));
            c->next = c2;
            c = c2;
            i = 0;
        }
        c->primes[i] = temp;
        i++;
        last = temp;
    }
    *out = head;

    fclose(f);
    return last;
}


int main() {
    printf("Generating primes database.\n");

    prime_chunk* head = NULL;
    int total = read_primes(&head);

    size_t datalen = sizeof(primesdb) + sizeof(prime_entry)*(total+1);
    primesdb* db = (primesdb*)malloc(datalen);
    prime_entry* entries = (prime_entry*)(db+sizeof(primesdb));
    db->max = total;
    
    int prev = -1;
    while(head) {
        // walk all the way through the current chunk 
        int j = 0;
        for(; j < PRIME_CHUNK_SIZE; j++) {
            if(prev == total) {
                // we're at the end of all of the primes
                break;
            }

            int p = head->primes[j];
            entries[p].prev = prev;
            entries[p].next = -1;
            
            // set the next link on the previous prime number 
            if(prev > 0) {
                entries[prev].next = p;
            }
            prev = p;
        }

        prime_chunk* n = head->next;
        free(head);
        head = n;
    }


    FILE* f = fopen("primes.dat", "w");
    if(!f) {
        fprintf(stderr, "Error creating primes.dat\n");
        exit(2);
    }
    fwrite(db, datalen, 1, f);

    fclose(f);
    free(db);
    return 0;
}
