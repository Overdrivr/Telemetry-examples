#include <Telemetry.h>

// Put writeable parameters in this struct
struct TM_state
{
  int32_t someParam;
};

// Function called each time a new frame is received by Telemetry
void on_new_frame(TM_state* state, TM_msg * msg){
  state->someParam += 1; // Received one more frame
}

Telemetry TM;
TM_state myParameters;

void setup() {
  // Init the writeable parameter
  myParameters.someParam = 0;
  
  TM.begin(115200);

  // Subscribe our function to be notified when a new frame is
  // received
  TM.sub(on_new_frame, &myParameters);
}

void loop() {
  TM.pub_i32("feedback",myParameters.someParam);
  TM.update();
  delay(10); 
}
