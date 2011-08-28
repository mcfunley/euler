#ifndef VECTOR_H
#define VECTOR_H


typedef struct {
    int size;
    int tail;
    int* entries;
} ivector;

typedef struct {
    ivector* v;
    int index;
} ivector_iter;


ivector* ivector_init(void);
void ivector_free(ivector* v);
int ivector_get(ivector* v, int i);
void ivector_set(ivector* v, int i, int x);
void ivector_append(ivector* v, int x);
void ivector_inc(ivector* v, int i);
int ivector_count(ivector* v);

ivector_iter* ivector_iter_init(ivector* v);
void ivector_iter_free(ivector_iter* iter);
int ivector_iter_next(ivector_iter* iter);
int ivector_iter_more(ivector_iter* iter);



#endif
