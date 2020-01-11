#include <AFMotor.h>
#include <SPI.h>
#define MAX_SPEED 0.4

int counter = 0;
char data[6];
 
#include <SoftwareSerial.h>
SoftwareSerial BTserial(A1, A2); // RX | TX
// Connect the HC-05 TX to Arduino pin A1 RX. 
// Connect the HC-05 RX to Arduino pin A2 TX through a voltage divider.
// 
 
char c = ' ';
AF_DCMotor motor1(3);
AF_DCMotor motor2(4);
void setup() 
{
  Serial.begin(9600);
    // HC-05 default serial speed for commincation mode is 9600
    BTserial.begin(9600);  
}
 
void loop()
{
 
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
              Serial.print(c);
              doSomething();
          } 
          else{
            data[counter] = c;
            counter++;
            Serial.print(c);
          }
        }
    } 
}
float rt2ov2 = sqrt(2)/2;
float hyp;

void doSomething(){
  int x = 0;
  int y = 0;
  x = ((data[0] - '0')) * (int)(26*MAX_SPEED);
  y = ((data[2] - '0')) * (int)(26*MAX_SPEED);

  if (x > 0)
    x += 21;
  if (y > 0)
    y += 21;
    
  if (data[1] == '1')
    motor1.run(BACKWARD);
  else
    motor1.run(FORWARD);

  if (data[3] == '1')
    motor2.run(BACKWARD);
  else
    motor2.run(FORWARD);
  motor1.setSpeed(x);
  motor2.setSpeed(y);

    Serial.print(x);
  Serial.write(", ");
  Serial.print(y);
  Serial.write("\n");
}

