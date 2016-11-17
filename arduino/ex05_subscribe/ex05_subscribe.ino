#include <Telemetry.h>

int32_t someParam = 0;

void setup() {
  Serial.begin(115200);

  // Attach variable someParam to topic "feedforward"
  Telemetry.attach_i32_to("feedforward", &someParam);
}

void loop() {
  Telemetry.pub_i32("feedback",someParam);
  // Update is required to update someParam when new data is received
  Telemetry.update();
  delay(10);
}
