#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "vector.h"


ivector* ivector_init() {
    int size = 1024;
    ivector* v = (ivector*)malloc(sizeof(ivector));
    if(!v) {
        perror("malloc failure - ivector");
        exit(1);
    }

    v->entries = (int*)malloc(sizeof(int)*size);
    if(!v->entries) {
        perror("malloc failure - ivector->entries");
        exit(1);
    }

    v->size = size;
    v->tail = -1;
    return v;
}


void ivector_free(ivector* v) {
    free(v->entries);
    free(v);
}


int ivector_get(ivector* v, int i) {
    return v->entries[i];
}


void ivector_inc(ivector* v, int i) {
    ivector_set(v, i, ivector_get(v, i)+1);
}


int ivector_count(ivector* v) {
    return v->tail + 1;
}

void ivector_expand(ivector* v) {
    int new_size = v->size * 2;
    int* new_entries = (int*)malloc(sizeof(int)*new_size);
    memcpy(new_entries, v->entries, v->size);
    
    v->entries = new_entries;
    v->size = new_size;
}


void ivector_set(ivector* v, int i, int x) {
    if(i >= v->size) { 
        ivector_expand(v);
    }
    v->entries[i] = x;

    if(i > v->tail) {
        v->tail = i;
    }
}


void ivector_append(ivector* v, int x) {
    ivector_set(v, v->tail + 1, x);
}


ivector_iter* ivector_iter_init(ivector* v) {
    ivector_iter* i = (ivector_iter*)malloc(sizeof(ivector_iter));
    if(!i) {
        perror("malloc error: ivector_iter");
        exit(1);
    }
    i->index = 0;
    i->v = v;
    return i;
}

void ivector_iter_free(ivector_iter* iter) {
    free(iter);
}

int ivector_iter_next(ivector_iter* iter) {
    return ivector_get(iter->v, iter->index++);
}


int ivector_iter_more(ivector_iter* iter) {
    return iter->index <= iter->v->tail ? 1 : 0;
}
