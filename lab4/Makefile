COMPILER = as
CMPFLAGS =
CMPFLAGSDEB = --gdwarf2
LINKER = ld
LNKFLAGS = -static
SOURCES=$(wildcard *.s)
OBJECTS=$(SOURCES:.s=.o)
EXE=$(SOURCES:.s=)

.PHONY: all clean

all: $(EXE)

$(EXE): %: %.o
	$(LINKER) $(LNKFLAGS) -o $@ $<

$(OBJECTS): %.o: %.s
	$(COMPILER) $(CMPFLAGS) -o $@ $<

dbg: l4.s
	$(COMPILER) $(CMPFLAGSDEB) -o l4.o -c $<
	$(LINKER) $(LNKFLAGS) -o dbg l4.o
cleandbg:
	rm dbg; rm l4.o
clean:
	rm $(EXE); rm $(OBJECTS)
