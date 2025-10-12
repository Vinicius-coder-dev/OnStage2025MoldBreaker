#include <Keyboard.h>
String command_detected;
String key_to_press;
char final_command;
void setup() {
  Serial.begin(115200);
  Keyboard.begin();
}

void loop() {
  key_to_press = "KEY_KP_";
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    command_detected = Serial.readStringUntil('\n');
  }
  if (command_detected != "") {
   //do things over here
   command_detected  "";
  }
}
