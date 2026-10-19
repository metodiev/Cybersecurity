#include <stdio.h>
#include <stdlib.h>

int global_initialized = 42;
int global_uninitialized;
static int static_value = 7;

__attribute__((noinline)) int add(int a, int b) {
    int local = a + b;
    return local;
}

int main(void) {
    int stack_value = add(2, 3);
    int *heap_value = malloc(sizeof(int));
    if (heap_value == NULL) return 1;
    *heap_value = 99;

    printf("add()        %p\n", (void *)&add);
    printf("static       %p\n", (void *)&static_value);
    printf("global init  %p\n", (void *)&global_initialized);
    printf("global bss   %p\n", (void *)&global_uninitialized);
    printf("heap         %p\n", (void *)heap_value);
    printf("stack        %p\n", (void *)&stack_value);
    printf("stack_value  %d\n", stack_value);
    free(heap_value);
    return 0;
}
