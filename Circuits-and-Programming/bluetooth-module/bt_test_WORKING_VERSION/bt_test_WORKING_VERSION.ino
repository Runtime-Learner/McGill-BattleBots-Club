#include <SPI.h>
#include <SoftwareSerial.h>

#define ledPin 7 // LED is connected to pin 7

SoftwareSerial BTserial(A1, 10); // RX | TX
// Connect the HC-05 TX to Arduino pin A1 RX. 
// Connect the HC-05 RX to Arduino pin 10 TX through a voltage divider.
 
void setup() {
    pinMode(ledPin, OUTPUT);
    
    // HC-05 default serial speed for commincation mode is 9600
    BTserial.begin(9600);
}

short c; //create a variable that will store the data received via bluetooth

void loop() {
    // Keep reading from HC-05 and turn LED on/off based on data received
    if (BTserial.available())
    {  
        c = BTserial.read();
        if (c == '1'){
          digitalWrite(ledPin, HIGH); //turn LED on
        }
        else if (c == '0'){
          digitalWrite(ledPin, LOW); //turn LED off
        }
    } 
}
