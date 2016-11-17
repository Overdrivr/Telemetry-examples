#include <Telemetry.h>

int8_t counter;

void setup() {
  Serial.begin(115200);
  counter = 0;
}

void loop() {
  Telemetry.pub_i8("counter",counter);
  counter++;
  delay(10); 
}
