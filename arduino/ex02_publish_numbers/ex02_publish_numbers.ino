#include <Telemetry.h>

Telemetry TM;
int8_t counter;

void setup() {
  TM.begin(115200);
  counter = 0;
}

void loop() {
  TM.pub_i8("counter",counter);
  counter++;
  delay(10); 
}
