#include <stdio.h>
#include <string.h>

__attribute__((noinline)) void copy_name(const char *input) {
    char buffer[16];
    strcpy(buffer, input);
    printf("name: %s\n", buffer);
}

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("usage: %s <name>\n", argv[0]);
        return 1;
    }
    copy_name(argv[1]);
    return 0;
}
