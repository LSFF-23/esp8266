#include <stdio.h>

// Seu código da função mostrar_status_ok() aqui

float calcular_distancia(float velocidade, float tempo) {
    return velocidade * tempo;
}

int main(void) {
    float distancia_percorrida;
    distancia_percorrida = calcular_distancia(10.5f, 2.0f);
    printf("Distância: %.1f m\n", distancia_percorrida);
    return 0;
}
