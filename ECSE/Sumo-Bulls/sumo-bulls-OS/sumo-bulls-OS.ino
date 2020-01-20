#include <SPI.h>
#include <SoftwareSerial.h>


#define MAX_SPEED 1

#define E1 6  // Enable Pin for motor 1
#define E2 3  // Enable Pin for motor 2
 
#define I1 5  // Control pin 1 for motor 1
#define I2 7  // Control pin 2 for motor 1
#define I3 2  // Control pin 1 for motor 2
#define I4 4  // Control pin 2 for motor 2


int counter = 0;
char data[6];
char c = ' ';

SoftwareSerial BTserial(A1, 10); // RX | TX
// Connect the HC-05 TX to Arduino pin A1 RX. 
// Connect the HC-05 RX to Arduino pin 10 TX through a voltage divider.
 
void setup() {
 
    pinMode(E1, OUTPUT);
    pinMode(E2, OUTPUT);
 
    pinMode(I1, OUTPUT);
    pinMode(I2, OUTPUT);
    pinMode(I3, OUTPUT);
    pinMode(I4, OUTPUT);

    // HC-05 default serial speed for commincation mode is 9600
    BTserial.begin(9600);
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
              doSomething();
          } 
          else{
            data[counter] = c;
            counter++;
          }
        }
    } 
}

int new1 = 0;
int new2 = 0;
int old1 = 0;
int old2 = 0;

void doSomething(){
  int x = 0;
  int y = 0;
  x = ((data[0] - '0')) * 26;
  y = ((data[2] - '0')) * 26;

  analogWrite(E1, 0);  // reduce back EMF when changing direction of motor spin
  analogWrite(E2, 0);  // by going to neutral state before doing so
  delay(20); //arduino crashes b/c of reversing motor directions. This is used to reduce the chances of that happening
  if (data[1] == '1'){
    digitalWrite(I2, HIGH); //H
    digitalWrite(I1, LOW); //L
    new1 = 1;
    
  }else{
    digitalWrite(I1, HIGH);
    digitalWrite(I2, LOW);
    new1 = -1;
  }

  if (data[3] == '1'){
    digitalWrite(I4, HIGH);
    digitalWrite(I3, LOW);
    new2 = 1;
  }else{
    digitalWrite(I3, HIGH);
    digitalWrite(I4, LOW);
    new2 = -1;
  }

  if (x > 0)
    x += 21;
  else
    new1 = 0;
  if (y > 0)
    y += 21;
  else new2 = 0;

  if (new1 != 0 && new2 != 0 && (new1 != old1 || new2 != old2)){
    analogWrite(E1, 10);  // electric braking
    analogWrite(E2, 10);  // electric braking
    delay(150); //give time to finish braking
  }
  old1 = new1;
  old2 = new2;

  analogWrite(E1, x);  // Run in full speed
  analogWrite(E2, y);  // Run in half speed
}
