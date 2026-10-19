CC ?= cc
CFLAGS ?= -O0 -g -Wall -Wextra

BINS = layout layout-nossp canary canary-nossp

.PHONY: all clean

all: $(BINS)

layout: layout.c
	$(CC) $(CFLAGS) -o $@ $<

layout-nossp: layout.c
	$(CC) $(CFLAGS) -fno-stack-protector -o $@ $<

canary: canary.c
	$(CC) $(CFLAGS) -fstack-protector-all -o $@ $<

canary-nossp: canary.c
	$(CC) $(CFLAGS) -fno-stack-protector -o $@ $<

clean:
	rm -f $(BINS)
	rm -rf $(addsuffix .dSYM,$(BINS))
