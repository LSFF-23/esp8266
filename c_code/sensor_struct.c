#include <stdio.h>

typedef struct {
    int id_sensor;
    float temperatura;
    float umidade;
} SensorData;

int main(void) {
    SensorData meu_sensor;
    meu_sensor.id_sensor = 101;
    meu_sensor.temperatura = 23.7f;
    meu_sensor.umidade = 68.2f;
    printf("ID: %d, Temp: %.1f, Umid: %.1f\n", meu_sensor.id_sensor, meu_sensor.temperatura, meu_sensor.umidade);
    return 0;
}
