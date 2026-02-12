AS   = mips-linux-gnu-as
LD   = mips-linux-gnu-ld

SRCS = $(wildcard *.s)
BINS = $(SRCS:.s=)

all: $(BINS)

%: %.s
	$(AS) -o $@.o $<
	$(LD) -o $@ $@.o

clean:
	rm -f *.o

purge:
	rm -f $(BINS) *.o