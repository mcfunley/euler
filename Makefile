CC=gcc
CFLAGS=-g -O3 -Wall
outdir=bin
objdir=obj


problems = \
  p0060


all: dirs primes.dat compile


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


$(objdir)/primesdb.o:
	$(CC) $(CFLAGS) -c primesdb.c -o $(objdir)/$$l.o


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

compile:
	@echo "Compiling sources"
	for p in $(problems) ; do \
		$(CC) $(CFLAGS) $$p.c $(objdir)/*.o -o $(outdir)/$$p ; \
	done

