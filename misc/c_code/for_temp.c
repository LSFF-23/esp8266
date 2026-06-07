#include <stdio.h>

int main(void) {
    float temperaturas[] = {22.5f, 23.0f, 21.8f, 24.1f};
    int i, tamanho = sizeof(temperaturas) / sizeof(temperaturas[0]);
    // Seu código aqui (laço for e impressão)
    for (i = 0; i < tamanho; i++)
        printf("Temperatura %d: %.1f\n", i, temperaturas[i]);
    return 0;
}