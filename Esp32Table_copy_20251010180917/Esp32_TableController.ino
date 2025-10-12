#include <AccelStepper.h>
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEScan.h>
#include <BLEAdvertisedDevice.h>
#define trigPin 32
#define echoPin 33

int8_t First_command;
int8_t Second_command;
int scanTime = 1;
int object_spin_time = 2000;  // in miliseconds
int trap_spin_time = 2000;    // in miliseconds
int plane_spin_time = 10000;   // in miliseconds
long timing;
bool trap_spin = false;
bool object_spin = false;
bool plane_spin = true;
int distance = 1000;
BLEScan *pBLEScan;
AccelStepper trap_stepper(AccelStepper::DRIVER, 5, 18);
AccelStepper object_stepper(AccelStepper::DRIVER, 4, 16);
AccelStepper plane_stepper(AccelStepper::DRIVER, 25, 26);

class MyAdvertisedDeviceCallbacks : public BLEAdvertisedDeviceCallbacks {
  void onResult(BLEAdvertisedDevice advertisedDevice) {
    //Serial.printf("Advertised Device: %s \n", advertisedDevice.toString().c_str());  // printa tudo
    String teste = advertisedDevice.getManufacturerData();
    //Serial.println(teste[0],HEX);
    //Serial.println(teste[1],HEX);
    if (teste[0] != 0x97) return;
    if (teste[1] != 0x03) return;
    //Serial.println(teste.length());
    if (teste.length() == 7) {
      First_command = teste[4];
      Second_command = teste[6];
      Serial.println(First_command);
      Serial.println(Second_command);
      // Commands to set the scenary
      if (First_command == 5) {
        if (Second_command == 1) {
          trap_spin = true;
        }
        if (Second_command == 2) {
          object_spin = true;
        }
        if (Second_command == 3) {
          plane_spin = true;
        }
      }
      BLEDevice::getScan()->stop();
    }
  }
};
void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  trap_stepper.setEnablePin(19);
  object_stepper.setEnablePin(17);
  plane_stepper.setEnablePin(27);
  trap_stepper.setMaxSpeed(2000);
  trap_stepper.setSpeed(2000);
  object_stepper.setMaxSpeed(1000);
  object_stepper.setSpeed(1000);
  plane_stepper.setMaxSpeed(2000);
  plane_stepper.setSpeed(2000);
  trap_stepper.disableOutputs();
  object_stepper.disableOutputs();
  plane_stepper.disableOutputs();
  Serial.begin(115200);
  Serial.println("Scanning...");
  
  BLEDevice::init("");
  pBLEScan = BLEDevice::getScan();  //create new scan
  pBLEScan->setAdvertisedDeviceCallbacks(new MyAdvertisedDeviceCallbacks(), true);
  pBLEScan->setActiveScan(true);  //active scan uses more power, but get results faster
  pBLEScan->setInterval(200);
  pBLEScan->setWindow(99);  // less or equal setInterval value
  delay(100);
}

void loop() {
  // start scaning here
  pBLEScan->start(scanTime, false); 
  //Serial.println(millis() - teste);
  pBLEScan->clearResults();  // delete results fromBLEScan buffer to release memory
  if (trap_spin == true) {
    trap_spin = false;
    //trap_stepper.enableOutputs();
    timing = millis();
    distance=20;
    while (lerUltra()>10){
      delay(10);
    }
    trap_stepper.enableOutputs();
    Serial.println("lkjh");
    timing = millis();
    while (millis() - timing < trap_spin_time) {
      trap_stepper.runSpeed();
      Serial.println("lkjh");
    }
    trap_stepper.disableOutputs();
  }
  if (object_spin == true) {
    object_spin = false;
    Serial.println("PO");
    object_stepper.enableOutputs();
    timing = millis();
    while (millis() - timing < object_spin_time) {
      object_stepper.runSpeed();
      Serial.println("ASDASD");
    }
    object_stepper.disableOutputs();
    delay(5000);
  }
  if (plane_spin == true) {
    plane_spin = false;
    plane_stepper.enableOutputs();
    timing = millis();
    while (millis() - timing < plane_spin_time) {
      plane_stepper.runSpeed();
      Serial.println("QW");
    }
   plane_stepper.disableOutputs();
  }
  delay(50);
}

int lerUltra() {
  // ultrasonic scan function
  long duration, distance;
  digitalWrite(trigPin, LOW);  // Added this line
  delayMicroseconds(2);        // Added this line
  digitalWrite(trigPin, HIGH);
  //  delayMicroseconds(1000); - Removed this line
  delayMicroseconds(10);  // Added this line
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration / 2) / 29.1;
  Serial.println(distance);
  return distance;
}
