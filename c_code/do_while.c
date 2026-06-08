#include <stdio.h>

int main(void) {
    int leitura_sensor;
    do {
        printf("Digite um valor de 0 a 100:\n");
        scanf("%d", &leitura_sensor);
    } while ((leitura_sensor < 0) || (leitura_sensor > 100));
    printf("Leitura válida: %d\n", leitura_sensor);
    return 0;
}