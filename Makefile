CC=gcc
CFLAGS=-g -pg -O3 -Wall -std=c99
outdir=bin
objdir=obj


libs = \
  vector \
  factorize \
  totient \
  permutation

problems = \
  p0060 \
  p0069 \
  totient_table \
  p0070 \
  sortchars_test \
  is_perm_test \
  p0072

all: dirs primes.dat print-primes compile-libs compile


dirs:
	if test ! -d $(outdir); then mkdir $(outdir); fi
	if test ! -d $(objdir); then mkdir $(objdir); fi


clean:
	rm -rf $(outdir)
	rm -rf $(objdir)
	rm -rf primes.txt
	rm -rf primes
	rm -rf primesdb
	rm -rf primes.dat
	rm -rf print-primes
	rm -rf primesdb-gen


print-primes: $(objdir)/primesdb.o print-primes.c
	$(CC) $(CFLAGS) print-primes.c $(objdir)/primesdb.o -o print-primes


$(objdir)/primesdb.o: primesdb.c primesdb.h
	$(CC) $(CFLAGS) -c primesdb.c -o $(objdir)/primesdb.o


primes.dat: primes.txt primesdb-gen 
	./primesdb-gen


primes:
	ghc -O primes.hs -o primes


primes.txt: primes
	@echo "Generating list of primes."; \
	./primes; 


primesdb-gen: $(objdir)/primesdb.o primesdb-gen.c
	$(CC) $(CFLAGS) primesdb-gen.c $(objdir)/primesdb.o -o primesdb-gen


primesdb-run:
	./primesdb-gen


compile-libs:
	@echo "Compiling libraries"
	for l in $(libs) ; do \
		$(CC) -c $(CFLAGS) $$l.c -o $(objdir)/$$l.o ; \
	done


compile:
	@echo "Compiling sources"
	for p in $(problems) ; do \
		$(CC) $(CFLAGS) $$p.c $(objdir)/*.o -o $(outdir)/$$p ; \
	done

