#include <Telemetry.h>

void setup() {
  Serial.begin(9600);
}

void loop() {
  Telemetry.pub("Hello","world");
  delay(1000);  // wait for a second
}
