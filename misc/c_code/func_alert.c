#include <stdio.h>

void verificar_alerta_temperatura(int temp_medida) {
    // Seu código aqui
    if (temp_medida > 100)
        printf("TEMPERATURA ALTA!\n");
}

int main() {
    int temperatura;
    
    scanf("%d", &temperatura);
    verificar_alerta_temperatura(temperatura);
    
    return 0;
}