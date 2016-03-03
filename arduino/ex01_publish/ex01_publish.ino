#include <Telemetry.h>

Telemetry TM;

void setup() {
  TM.begin(9600);
}

void loop() {
  TM.pub("Hello","world");
  delay(1000);  // wait for a second
}
