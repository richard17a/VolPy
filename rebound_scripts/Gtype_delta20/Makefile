export OPENGL=0
export OPENMP=0
export PROFILING=0
include ../rebound_src/Makefile.defs

all: librebound
	@echo ""
	@echo "Compiling problem file ..."
	$(CC) -I../rebound_src/ -Wl,-rpath,./ $(OPT) $(PREDEF) problem.c -L. -lrebound $(LIB) -o rebound
	@echo ""
	@echo "REBOUND compiled successfully."

librebound: 
	@echo "Compiling shared library librebound.so ..."
	$(MAKE) -C ../rebound_src/
	@-rm -f librebound.so
	@ln -s ../../../src/librebound.so .

clean:
	@echo "Cleaning up shared library librebound.so ..."
	@-rm -f librebound.so
	$(MAKE) -C ../rebound_src/ clean
	@echo "Cleaning up local directory ..."
	@-rm -vf rebound
