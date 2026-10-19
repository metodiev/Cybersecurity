#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "usage: %s <path>\n", argv[0]);
        return 2;
    }

    int fd = open(argv[1], O_RDONLY);
    if (fd < 0) {
        fprintf(stderr, "open failed: %s (errno=%d)\n", strerror(errno), errno);
        return 1;
    }

    char buffer[16];
    ssize_t n = read(fd, buffer, sizeof(buffer));
    if (n < 0) {
        fprintf(stderr, "read failed: %s (errno=%d)\n", strerror(errno), errno);
        close(fd);
        return 1;
    }

    ssize_t written = write(STDOUT_FILENO, buffer, (size_t)n);
    if (written < 0) {
        fprintf(stderr, "write failed: %s (errno=%d)\n", strerror(errno), errno);
    }

    close(fd);
    return 0;
}
