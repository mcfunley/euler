#include "euler.h"

int comparechars(const void* a, const void* b) {
    return *(const char*)a - *(const char*)b;
}


void sortchars(char* c) {
    qsort(c, strlen(c), sizeof(char), comparechars);
}


int is_perm(int i, int j) {
    char is[64], js[64];
    sprintf(is, "%d", i);
    sprintf(js, "%d", j);
    sortchars(is);
    sortchars(js);
    return strcmp(is, js) == 0;
}
