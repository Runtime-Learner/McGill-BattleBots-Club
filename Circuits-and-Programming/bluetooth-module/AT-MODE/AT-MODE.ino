// Basic Bluetooth sketch HC-05_02
// Connect the HC-05 module and communicate using the serial monitor
//
// The HC-05 defaults to commincation mode when first powered on.
// The default baud rate for communication mode is 9600
// 
#define ledPin 7
int state = 0;

 
#include <SoftwareSerial.h>
SoftwareSerial BTserial(2, 3); // RX | TX
// Connect the HC-05 TX to Arduino pin 2 RX. 
// Connect the HC-05 RX to Arduino pin 3 TX through a voltage divider.
// 
 
char c = ' ';
 
void setup() 
{
    pinMode(ledPin, OUTPUT);
    digitalWrite(ledPin, HIGH);

    
    Serial.begin(38400);
    Serial.println("Arduino is ready");

    // HC-05 default serial speed for commincation mode is 9600
    BTserial.begin(38400);
}
 
void loop()
{
 
    // Keep reading from HC-05 and send to Arduino Serial Monitor
    if (BTserial.available())
    {  
        c = BTserial.read();
        if (c == '1'){
          digitalWrite(ledPin, HIGH);
        }
        else{
          digitalWrite(ledPin, LOW);
        }
        Serial.write(c);
    }
 
    // Keep reading from Arduino Serial Monitor and send to HC-05
    if (Serial.available())
    {
        c =  Serial.read();
        BTserial.write(c);  
    }
 
}
