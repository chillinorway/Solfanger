#include <OneWire.h>
#include <DallasTemperature.h>

#include <CircusESP32Lib.h>

// ------------------------------------------------
// These are the CircusESP32Lib related declarations
// ------------------------------------------------

char ssid[] = "www.internett.com"; // Place your wifi SSID here
char password[] =  "WtpEL32779"; // Place your wifi password here
char token[] = "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxMDQ4MCJ9.GU3O0z-pzanp-l8LlIIv26Z7YKu3UpxwrA3V203eeyk"; // Place your token, find it in 'account' at Circus. It will identify you.
char server[] = "www.circusofthings.com";
char temp_kammer_key[] = "5312"; // Type the Key of the Circus Signal you want the ESP32 listen to.
char mengde_key[] = "12544";
char temp_ut_key[] = "30893";
char temp_inn_key[] = "16251";
char ambient_temp_key[] = "13452";

CircusESP32Lib circusESP32(server, ssid, password); // The object representing an ESP32 to whom you can order to Write or Read


// Data wire is plugged into port 2 on the Arduino
#define ONE_WIRE_BUS 4

// Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);

// Pass our oneWire reference to Dallas Temperature.
DallasTemperature sensors(&oneWire);

// arrays to hold device address
DeviceAddress inputThermometer = { 0x28, 0xFF, 0x64, 0x06, 0xC6, 0x44, 0x28, 0x8C };
DeviceAddress outputThermometer = { 0x28, 0xFF, 0x64, 0x06, 0xC1, 0x51, 0x69, 0xFD };
DeviceAddress chamberThermometer = { 0x28, 0xFF, 0x64, 0x06, 0xC6, 0x55, 0xC5, 0xB0 };
DeviceAddress outsideThermometer = { 0x28, 0xFF, 0x64, 0x06, 0xC6, 0x55, 0xC5, 0xB0 };

const byte flip = 2;
volatile int count = 0;

float litre = 0.0;
double amount;

unsigned long update_ticker;
unsigned long update_interval = 1000L;

void setup() {
  // put your setup code here, to run once:
  pinMode(flip, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(flip), counter, FALLING);

  circusESP32.begin(); // Let the Circus object set up itself for an SSL/Secure connection
  // Serial monitor setup
  Serial.begin(115200);
  sensors.begin();
  Serial.print("Found ");
  Serial.print(sensors.getDeviceCount(), DEC);

  sensors.setResolution(inputThermometer, 9);
  sensors.setResolution(outputThermometer, 9);
  sensors.setResolution(chamberThermometer, 9);
  sensors.setResolution(outsideThermometer, 9);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  if (millis() - update_ticker > update_interval) {
    // Get flow data
    amount = ((count) / 430.0)  * 1000; //217
    Serial.print(amount);
    Serial.println();
    // Get temperature data
    sensors.requestTemperatures();
    float tempC = sensors.getTempC(chamberThermometer);
    float temp_inn = sensors.getTempC(inputThermometer);
    float temp_ut = sensors.getTempC(outputThermometer);
    float ambient = sensors.getTempC(outsideThermometer);
    
    circusESP32.write(temp_kammer_key, tempC, token); // Report the temperature measured to Circus.
    circusESP32.write(mengde_key, amount, token); // Report the humidity measured to Circus.
    circusESP32.write(temp_ut_key, temp_ut, token); // Report the humidity measured to Circus.
    circusESP32.write(temp_inn_key, temp_inn, token); // Report the humidity measured to Circus.
    circusESP32.write(ambient_temp_key, ambient, token); // Report the humidity measured to Circus.
    /*
      printTemperature(inputThermometer);
      Serial.print("\t");
      printTemperature(outputThermometer);
      Serial.print("\t");
      printTemperature(chamberThermometer);
      Serial.print("\t");

    */
    count = 0;
    update_ticker = millis();

  }

}

void counter() {
  detachInterrupt(digitalPinToInterrupt(flip));
  count++;
  attachInterrupt(digitalPinToInterrupt(flip), counter, FALLING);
}

// function to print the temperature for a device
void printTemperature(DeviceAddress deviceAddress)
{
  float tempC = sensors.getTempC(deviceAddress);
  if (tempC == DEVICE_DISCONNECTED_C)
  {
    Serial.println("Error: Could not read temperature data");
    return;
  }
  Serial.print(tempC);
}
