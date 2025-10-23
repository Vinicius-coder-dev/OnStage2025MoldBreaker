#include <Ticker.h>

/*
    Based on Neil Kolban example for IDF: https://github.com/nkolban/esp32-snippets/blob/master/cpp_utils/tests/BLE%20Tests/SampleServer.cpp
*/
#define RXD2 16
#define TXD2 17
//Librarys used to broadcast and make servers
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>
#include <BLEAdvertising.h>
BLEAdvertisementData pAdvertisementData;
BLEAdvertising *pAdvertising;
// See the following for generating UUIDs:
// https://www.uuidgenerator.net/

// Command list, in which 0 means it ended
char cards_commands[52][10] = {
  { 0x05, 0x02, 0x01, 0x04, 0x02, 0x06, 0x03, 0x09, 0x06, 0x00}// Start history 1
  { 0x06, 0x01, 0x02, 0x08, 0, 0, 0 ,0 ,0, 0 },// Choice 1 history 1
  { 0x06, 0x02, 0x02, 0x03, 0x04, 0x05, 0, 0, 0, 0 },// Choice 2 history 1
  { 0x06, 0x03, 0x02, 0x0A, 0x05, 0x01, 0x01, 0x0E, 0, 0 },// Continuation choice 1 history 1
  { 0x06, 0x04, 0x02, 0x0B, 0x03, 0x0C, 0x04, 0x0D, 0, 0 },// Continuation choice 2 history 1
  { 0x06, 0x05, 0, 0, 0, 0, 0, 0, 0, 0},
  { 0x06, 0x06, 0, 0, 0, 0, 0, 0, 0, 0}, // Choice 2 history 2
  { 0x06, 0x07, 0, 0, 0, 0, 0, 0, 0, 0}, // Start history 2
  { 0x06, 0x08, 0, 0, 0, 0, 0, 0, 0, 0}, // Extra commands not utilized
  { 0x06, 0x09, 0, 0, 0, 0, 0, 0, 0, 0},
  { 0x06, 0x0A, 0, 0, 0, 0, 0, 0, 0, 0},
  { 0x06, 0x0B, 0, 0, 0, 0, 0, 0, 0, 0},
  { 0x06, 0x0C, 0, 0, 0, 0, 0, 0, 0, 0},
  { 0x06, 0x0D, 0x05, 0x04, 0, 0, 0, 0, 0, 0}, // Command to start the choice in the screen
  { 0x06, 0x0E, 0, 0, 0, 0, 0, 0, 0, 0},
  { 0x06, 0x0F, 0, 0, 0, 0, 0, 0, 0, 0}, // End and thanking
  { 0x06, 0x10, 0, 0, 0, 0, 0, 0, 0, 0}, // Choice 1 history 2
  { 0x06, 0x11, 0, 0, 0, 0, 0, 0, 0, 0}, // Continuation choice 1 history 2 // not utilized
  { 0x06, 0x12, 0, 0, 0, 0, 0 ,0 ,0 ,0} // Continuation choice 2 history 2 // not utilized
};
#define SERVICE_UUID "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define CHARACTERISTIC_UUID "beb5483e-36e1-4688-b7f5-ea07361b26a8"

void setup() {
  Serial2.begin(115200, SERIAL_8N1, RXD2, TXD2);
  Serial.begin(115200);
  delay(1000);
  Serial.println("Starting Arduino BLE Client application...");
  //Server creation occurs here
  BLEDevice::init("ESP32-scale");
  BLEServer *pServer = BLEDevice::createServer();
  pAdvertising = pServer->getAdvertising();
  //pAdvertising->start();
}

void loop() {
  String card_detected = "";
  //Receives the command from UART
  if (Serial.available()) {
    card_detected = Serial.readStringUntil('\n');
  }
  //Serial.println(card_detected);

  if (card_detected != "") {

    int number_of_commands = 0;
    // Finding the number of commands necessary to broadcast
    for (int y = 0; y < 10; y++) {
      if (cards_commands[card_detected.toInt()][y] != 0) {
        number_of_commands++;
      } else {
        break;
      }
    }
    Serial.println(number_of_commands);
    //Finding commands to broadcast
    for (int i = 0; i < number_of_commands; i += 2) {
      BLEAdvertisementData advdata = BLEAdvertisementData();
      String sending_vector = "";

      char sending[7];
      //Setting the string to match the model of Spike
      sending[0] = 0x97; //
      sending[1] = 0x03; // 
      sending[2] = 0x01; // The channel number, in this case 1
      sending[3] = 0x61; //
      sending[5] = 0x61; // 



      sending[4] = cards_commands[card_detected.toInt()][i];
      sending[6] = cards_commands[card_detected.toInt()][i + 1];
      sending_vector = String(sending);
      Serial.println(sending_vector[4], HEX);
      Serial.println(sending_vector[6], HEX);

      advdata.setManufacturerData(String(sending, 7));
      pAdvertising->setAdvertisementData(advdata);
      pAdvertising->start();
      delay(800);
      pAdvertising->stop();
      delay(100);
    }
  }
}
