#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEScan.h>
#include <BLEAdvertisedDevice.h>
#define RXD2 16
#define TXD2 17
BLEScan *pBLEScan;
int8_t First_command;
int8_t Second_command;
int scanTime = 1;
String command_toSend;
String command_detected;
class MyAdvertisedDeviceCallbacks : public BLEAdvertisedDeviceCallbacks {
  void onResult(BLEAdvertisedDevice advertisedDevice) {
    //Serial.printf("Advertised Device: %s \n", advertisedDevice.toString().c_str());  // printa tudo
    String teste = advertisedDevice.getManufacturerData();
    //Serial.println(teste[0],HEX);
    //Serial.println(teste[1],HEX);
    if (teste[0] != 0x97) return;
    if (teste[1] != 0x03) return;
    Serial.println(teste.length());
    if (teste.length() == 7) {
      First_command = teste[4];
      Second_command = teste[6];
      if (First_command == 6) {
          command_toSend = String(Second_command);
      }
    
    }
  }
};
void setup() {
  Serial2.begin(115200, SERIAL_8N1, RXD2, TXD2);
  Serial.begin(115200);
  Serial.println("Scanning...");

  BLEDevice::init("");
  pBLEScan = BLEDevice::getScan();  //create new scan
  pBLEScan->setAdvertisedDeviceCallbacks(new MyAdvertisedDeviceCallbacks());
  pBLEScan->setActiveScan(true);  //active scan uses more power, but get results faster
  pBLEScan->setInterval(100);
  pBLEScan->setWindow(99);  // less or equal setInterval value


}

void loop() {

  BLEScanResults *foundDevices = pBLEScan->start(scanTime, false);
  Serial.print("Devices found: ");
  Serial.println(foundDevices->getCount());
  Serial.println("Scan done!");
  pBLEScan->clearResults();  // delete results fromBLEScan buffer to release memory

  if (Serial2.available()) {
    command_detected = Serial.readStringUntil('\n');
  }
  if (command_toSend != "") {
    Serial2.println(command_toSend);
    command_toSend = "";
  }
}
