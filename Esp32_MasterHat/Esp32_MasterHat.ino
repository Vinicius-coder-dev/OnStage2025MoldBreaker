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

// Lista dos comandos, em que 0 siginifica que os comandos acaba ali
char cards_commands[52][10] = {
  { 0x05, 0x02, 0x01, 0x04, 0x02, 0x06, 0x03, 0x09, 0x06, 0x00}// Começo história 1,
  { 0x06, 0x01, 0x02, 0x08, 0, 0, 0 ,0 ,0, 0 },// Escolha 1 história 1
  { 0x06, 0x02, 0x02, 0x03, 0x04, 0x05, 0, 0, 0, 0 },// Escolha 2 história 1
  { 0x06, 0x03, 0x02, 0x0A, 0x05, 0x01, 0x01, 0x0E, 0, 0 },// Continuação escolha 1 história 1
  { 0x06, 0x04, 0x02, 0x0B, 0x03, 0x0C, 0x04, 0x0D, 0, 0 },// Continuaçaõ escolha 2 história 1
  { 0x06, 0x05, 0, 0, 0, 0, 0, 0, 0, 0},
  { 0x06, 0x06, 0, 0, 0, 0, 0, 0, 0, 0}, // Escolha 2 história 2
  { 0x06, 0x07, 0, 0, 0, 0, 0, 0, 0, 0}, // Começo história 2
  { 0x06, 0x08, 0, 0, 0, 0, 0, 0, 0, 0},
  { 0x06, 0x09, 0, 0, 0, 0, 0, 0, 0, 0},
  { 0x06, 0x0A, 0, 0, 0, 0, 0, 0, 0, 0},
  { 0x06, 0x0B, 0, 0, 0, 0, 0, 0, 0, 0},
  { 0x06, 0x0C, 0, 0, 0, 0, 0, 0, 0, 0},
  { 0x06, 0x0D, 0x05, 0x04, 0, 0, 0, 0, 0, 0},
  { 0x06, 0x0E, 0, 0, 0, 0, 0, 0, 0, 0},
  { 0x06, 0x0F, 0, 0, 0, 0, 0, 0, 0, 0}, // Final e agradecimentos
  { 0x06, 0x10, 0, 0, 0, 0, 0, 0, 0, 0}, // Escolha 1 história 2
  { 0x06, 0x11, 0, 0, 0, 0, 0, 0, 0, 0}, // Continuação escolha 1 história 2
  { 0x06, 0x12, 0, 0, 0, 0, 0 ,0 ,0 ,0} // Continuação escolha 2 história 2
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
  //Verifica o UART da Raspberry
  if (Serial.available()) {
    card_detected = Serial.readStringUntil('\n');
  }
  //Serial.println(card_detected);
  //Cards detection occurs here

  if (card_detected != "") {

    int number_of_commands = 0;
    // Quantos comandos serão enviados
    for (int y = 0; y < 10; y++) {
      if (cards_commands[card_detected.toInt()][y] != 0) {
        number_of_commands++;
      } else {
        break;
      }
    }
    Serial.println(number_of_commands);
    //Lendo a lista de comandos de acordo com o número encontrado acima
    for (int i = 0; i < number_of_commands; i += 2) {
      BLEAdvertisementData advdata = BLEAdvertisementData();
      String sending_vector = "";

      char sending[7];
      //Setting the string to match the model of Spike
      sending[0] = 0x97;
      sending[1] = 0x03;
      sending[2] = 0x01;
      sending[3] = 0x61;
      sending[5] = 0x61;



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
