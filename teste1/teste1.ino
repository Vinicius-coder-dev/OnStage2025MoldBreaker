#include <Ultrasonic.h>

#include <AccelStepper.h>
#include <MultiStepper.h>

#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEScan.h>
#include <BLEAdvertisedDevice.h>


#define trigPin 32
#define echoPin 33

int object_spin_time = 1;  // in seconds
int trap_spin_time = 1;    // in seconds
int plane_spin_time = 1;   // in seconds
long long timing = 0;
int distance;
volatile bool trap_spin = false;
volatile bool object_spin = true;
volatile bool plane_spin = false;

AccelStepper trap_stepper(AccelStepper::DRIVER, 5, 18);
AccelStepper object_stepper(AccelStepper::DRIVER, 4, 16);
AccelStepper plane_stepper(AccelStepper::DRIVER, 25, 26);

void setup() {
  Serial.begin(9600);
  trap_stepper.setEnablePin(19);
  object_stepper.setEnablePin(17);
  plane_stepper.setEnablePin(27);
  trap_stepper.setMaxSpeed(400);
  trap_stepper.setSpeed(400);
  object_stepper.setMaxSpeed(400);
  object_stepper.setSpeed(400);
  plane_stepper.setMaxSpeed(400);
  plane_stepper.setSpeed(400);
  trap_stepper.disableOutputs();
  object_stepper.disableOutputs();
  plane_stepper.enableOutputs();
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}


void loop() {
  distance = lerUltra();
  Serial.println(distance);
  delay(400);
  //plane_stepper.runSpeed();
  /*if (trap_spin == true) {
    trap_spin = false;
    timing = millis();
    trap_stepper.moveTo(180);
  }
  if (object_spin == true) {
    object_spin = false;
    timing = millis();
      object_stepper.moveTo(180);
  }*/
}

long lerUltra() {
  long duration, distance;
  digitalWrite(trigPin, LOW);  // Added this line
  delayMicroseconds(2);        // Added this line
  digitalWrite(trigPin, HIGH);
  //  delayMicroseconds(1000); - Removed this line
  delayMicroseconds(10);  // Added this line
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration / 2) / 29.1;
  return distance;
}