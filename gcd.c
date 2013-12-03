
int gcd(int a, int b) {
    while(a != b) {
        if(b > a) {
            b = b - a;
        } else {
            a = a - b;
        }
    }
    return a;
}
