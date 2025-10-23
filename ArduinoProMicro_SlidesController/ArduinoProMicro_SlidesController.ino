#include <SoftwareSerial.h>
#include <Keyboard.h>


String command_detected;
String key_to_press;
char final_command;


SoftwareSerial mySerial = SoftwareSerial(8, 9);

void setup() {

  mySerial.begin(9600);
  Serial.begin(115200);
  Keyboard.begin();
  delay(4000);
  Keyboard.press(KEY_LEFT_GUI); // test 
  Keyboard.releaseAll();
}

void loop() {
  key_to_press = "KEY_KP_";
  if (mySerial.available()) {
    command_detected = mySerial.readString();
    Serial.println(command_detected);
  }
  if (Serial.available()) {
    String test = Serial.readStringUntil('\n');
    Serial.println(test);
    mySerial.println(test);
  }
  if (command_detected != "") {
    //Start choice
    if (command_detected == "13") {
      Serial.println(command_detected);
      Keyboard.press(KEY_KP_2);
      delay(100);
      Keyboard.press(KEY_RETURN);
      Keyboard.releaseAll();
      command_detected = "";
    }
    //First command  
   if (command_detected == "0") {
      Serial.println(command_detected);
      Keyboard.press(KEY_KP_4);
      delay(100);
      Keyboard.press(KEY_RETURN);
      Keyboard.releaseAll();
      command_detected = "";
    }
    //First history AI call
   if (command_detected == "14") {
      Serial.println(command_detected);
      Keyboard.press(KEY_KP_4);
      delay(10);
      Keyboard.press(KEY_RETURN);
      delay(10);
       Keyboard.releaseAll();
      delay(29500);
      Keyboard.press(KEY_KP_ASTERISK);
      delay(100);
      Keyboard.releaseAll();
      delay(200);
      Keyboard.releaseAll();
      command_detected = "";
    }
    // First history choice 1
    if (command_detected == "2") {
      Serial.println(command_detected);
      Keyboard.releaseAll();
      Keyboard.press(KEY_KP_1);
      Keyboard.press(KEY_KP_2);
      delay(100);
      Keyboard.press(KEY_RETURN);
      delay(500);
      Keyboard.releaseAll();
       Keyboard.press(KEY_KP_DOT);
      delay(200);
       Keyboard.releaseAll();
      command_detected = "";
    }
    //First history choice 2
    if (command_detected == "1") {
      Serial.println(command_detected);
      Keyboard.releaseAll();
      Keyboard.press(KEY_KP_1);
      Keyboard.press(KEY_KP_4);
      delay(10);
      Keyboard.press(KEY_RETURN);
      delay(500);
       Keyboard.releaseAll();
       Keyboard.press(KEY_KP_DOT);
      delay(200);
       Keyboard.releaseAll();
      command_detected = "";
    }
    //End and thanking
    if (command_detected == "15") {
      Serial.println(command_detected);
      Keyboard.releaseAll();
      Keyboard.press(KEY_KP_2);
      Keyboard.press(KEY_KP_3);
      delay(10);
      Keyboard.press(KEY_RETURN);
      delay(10);
       Keyboard.releaseAll();
       Keyboard.press(KEY_KP_DOT);
      delay(200);
       Keyboard.releaseAll();
      command_detected = "";
    }
    //Second history
    if (command_detected == "7") {
      Serial.println(command_detected);
      Keyboard.releaseAll();
      Keyboard.press(KEY_KP_1);
      Keyboard.press(KEY_KP_7);
      delay(10);
      Keyboard.press(KEY_RETURN);
      delay(10);
       Keyboard.releaseAll();
       Keyboard.press(KEY_KP_DOT);
      delay(200);
       Keyboard.releaseAll();
      command_detected = "";
    }
    //Second history AI call
    if (command_detected == "8") {
      Serial.println(command_detected);
      Keyboard.releaseAll();
      Keyboard.press(KEY_RIGHT_ARROW);
      delay(10);
       Keyboard.releaseAll();
      delay(19800);
      Keyboard.press(KEY_KP_ASTERISK);
      delay(100);
      Keyboard.releaseAll();
      delay(200);
      Keyboard.releaseAll();
      command_detected = "";
      command_detected = "";
    }
    //Second history choice 1
    if (command_detected == "16") {
      Serial.println(command_detected);
      Keyboard.releaseAll();
      Keyboard.press(KEY_KP_2);
      Keyboard.press(KEY_KP_1);
      delay(10);
      Keyboard.press(KEY_RETURN);
      delay(50);
       Keyboard.releaseAll();
       Keyboard.press(KEY_KP_DOT);
      delay(200);
       Keyboard.releaseAll();
      command_detected = "";
    }
    //Second history choice 2
    if (command_detected == "6") {
      Serial.println(command_detected);
      Keyboard.releaseAll();

      Keyboard.press(KEY_KP_2);
      Keyboard.press(KEY_KP_3);
      delay(10);
      Keyboard.press(KEY_RETURN);
      delay(50);
       Keyboard.releaseAll();
       Keyboard.press(KEY_KP_DOT);
      delay(200);
       Keyboard.releaseAll();
      command_detected = "";
    }
  }
}
