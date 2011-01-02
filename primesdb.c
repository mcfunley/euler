#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include "primesdb.h"


prime_entry* primesdb_entries(primesdb* db) {
    return (prime_entry*)(db + sizeof(primesdb));
}


void primesdb_free(primesdb* db) {
    int fd = db->filedesc;
    munmap((void*)db, db->sz);
    close(fd);
}


primesdb* primesdb_init() {
    int fd = open("primes.dat", O_RDWR);
    if(fd < 0) {
        perror("Error opening primes.dat.");
        exit(1);
    }

    struct stat sb = {0};
    if(fstat(fd, &sb) == -1) {
        perror("fstat");
        exit(1);
    }

    void* p = mmap(0, sb.st_size, PROT_READ|PROT_WRITE, MAP_SHARED, fd, 0);
    if(p == MAP_FAILED) {
        perror("mmap");
        exit(1);
    }

    primesdb* db = (primesdb*)p;
    db->filedesc = fd;
    db->sz = sb.st_size;
    return db;
}



void prime_iter_init(prime_iter* it, primesdb* db) {
    it->p = 2;
    it->db = db;
}


int prime_iter_next(prime_iter* it) {
    int p = it->p;
    it->p = primesdb_entries(it->db)[p].next;
    return p;
}


int primesdb_is_prime(primesdb* db, int i) {
    if(i > db->max) {
        return 0;
    }
    prime_entry e = primesdb_entries(db)[i];
    return (e.next != 0 && e.prev != 0) ? 1 : 0;
}
