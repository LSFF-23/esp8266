#include <stdio.h>

int main(void) {
    int i = 0;
    while (i <= 9) {
        i = i + 1;
        if (i % 2 == 0)
            continue;
        printf("%d\n", i);
    }
    return 0;
}
