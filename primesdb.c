#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include "primesdb.h"


primesdb* g_primes = 0;


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



inline primesdb* _primesdb() {
    if(!g_primes) {
        g_primes = primesdb_init();
    }
    return g_primes;
}

inline prime_entry* primesdb_entries() {
    return (prime_entry*)(_primesdb() + sizeof(primesdb));
}


void primesdb_free() {
    if(g_primes) {
        int fd = g_primes->filedesc;
        munmap((void*)g_primes, g_primes->sz);
        close(fd);
        g_primes = 0;
    }
}



void prime_iter_init(prime_iter* it) {
    it->p = 2;
    it->db = _primesdb();
}


int prime_iter_next(prime_iter* it) {
    int p = it->p;
    it->p = primesdb_entries()[p].next;
    return p;
}


int primesdb_is_prime(int i) {
    primesdb* db = _primesdb();
    if(i > db->max) {
        return 0;
    }
    prime_entry e = primesdb_entries()[i];
    return (e.next != 0 && e.prev != 0) ? 1 : 0;
}
