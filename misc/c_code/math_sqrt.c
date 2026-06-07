#include <stdio.h>
// Inclua a biblioteca math.h aqui
#include <math.h>

int main(void) {
    float valor = 25.0f;
    float raiz_quadrada;
    // Seu código aqui (uso de sqrt e printf)
    raiz_quadrada = (float)sqrt((double) valor);
    printf("Raiz quadrada: %.2f", raiz_quadrada);
    return 0;
}
