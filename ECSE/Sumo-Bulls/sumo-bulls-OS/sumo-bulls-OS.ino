#include <SPI.h>
#define MAX_SPEED 1

int counter = 0;
char data[6];
 
#include <SoftwareSerial.h>
SoftwareSerial BTserial(A1, 10); // RX | TX
// Connect the HC-05 TX to Arduino pin A1 RX. 
// Connect the HC-05 RX to Arduino pin 10 TX through a voltage divider.
// 
 
char c = ' ';


#define E1 6  // Enable Pin for motor 1
#define E2 3  // Enable Pin for motor 2
 
#define I1 5  // Control pin 1 for motor 1
#define I2 7  // Control pin 2 for motor 1
#define I3 2  // Control pin 1 for motor 2
#define I4 4  // Control pin 2 for motor 2
 
void setup() {
 
    pinMode(E1, OUTPUT);
    pinMode(E2, OUTPUT);
 
    pinMode(I1, OUTPUT);
    pinMode(I2, OUTPUT);
    pinMode(I3, OUTPUT);
    pinMode(I4, OUTPUT);

    // HC-05 default serial speed for commincation mode is 9600
    BTserial.begin(9600);
//    Serial.begin(9600);
}
 
void loop() {
    // Keep reading from HC-05 and send to Arduino Serial Monitor
    if (BTserial.available())
    {  
        c = BTserial.read();
        if (c == '!'){
          counter = 0;
        }
        else{
          if (counter > 2){
            if(counter == 3)
              data[counter] = c;
//              Serial.print(c);
              doSomething();
          } 
          else{
            data[counter] = c;
            counter++;
//            Serial.print(c);
          }
        }
    } 
}

void doSomething(){
  int x = 0;
  int y = 0;
  x = ((data[0] - '0')) * 26;
  y = ((data[2] - '0')) * 26;

  if (x > 0)
    x += 21;
  if (y > 0)
    y += 21;

  analogWrite(E1, 0);  // reduce back EMF when changing direction of motor spin
  analogWrite(E2, 0);  // by going to neutral state before doing so
  delay(20); //arduino crashes b/c of reversing motor directions. This is used to reduce the chances of that happening
  if (data[1] == '1'){
    digitalWrite(I1, LOW); //L
    digitalWrite(I2, HIGH); //H
  }else{
    digitalWrite(I1, HIGH);
    digitalWrite(I2, LOW);
  }

  if (data[3] == '1'){
    digitalWrite(I3, LOW);
    digitalWrite(I4, HIGH);
  }else{
    digitalWrite(I3, HIGH);
    digitalWrite(I4, LOW);
  }

  analogWrite(E1, x);  // Run in full speed
  analogWrite(E2, y);  // Run in half speed

//  Serial.print(", ");
//  Serial.print(data[1]);
//  Serial.write(", ");
//  Serial.print(data[3]);
//  Serial.write("\n");
}
