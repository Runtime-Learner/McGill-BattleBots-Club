/*
 Controlling a servo position using a potentiometer (variable resistor)
 by Michal Rinott <http://people.interaction-ivrea.it/m.rinott>

 modified on 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Knob
*/

/*
Code edited to support a variable resistance range
(using graphite on paper as a potentiometer substitute)
*/

#include <Servo.h>

Servo myservo;  // create servo object to control a servo

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//ENTER YOUR VALUES HERE
int lowInput = 600;
int highInput = 720;
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

int potpin = 0;  // analog pin used to connect the potentiometer
int val;    // variable to read the value from the analog pin

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  pinMode(potpin, INPUT); //set pin A0 to be an input pin.
                                  //and set it to standby at 5V
  Serial.begin(9600); //begin a serial connection with the computer
}

void loop() {
  
  val = analogRead(potpin);            // reads the value of the 'potentiometer' (value between lowInput and highInput)
  Serial.print(val); //write the value of the input pin to the computer
  Serial.print("\n");
  val = map(val, lowInput, highInput, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
  myservo.write(val);                  // sets the servo position according to the scaled value
  delay(100);                           // waits for the servo to get there
}
