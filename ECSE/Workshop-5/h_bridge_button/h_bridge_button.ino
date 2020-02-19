#define E1 6  // Enable Pin for motor 1
#define E2 3  // Enable Pin for motor 2
 
#define I1 5  // Control pin 1 for motor 1
#define I2 7  // Control pin 2 for motor 1
#define I3 2  // Control pin 1 for motor 2
#define I4 4  // Control pin 2 for motor 2

#define buttonPin A5     //pin on which the button will be connected

boolean motorState = LOW;

void setup() {
    pinMode(E1, OUTPUT);
    pinMode(E2, OUTPUT);
 
    pinMode(I1, OUTPUT);
    pinMode(I2, OUTPUT);
    pinMode(I3, OUTPUT);
    pinMode(I4, OUTPUT);


    pinMode(buttonPin, INPUT_PULLUP); //button pin is input. Set it to be 5V standby
}
 
void loop() {
    if (motorState != digitalRead(buttonPin))
    {
      // change direction
   
      digitalWrite(E1, LOW);
      digitalWrite(E2, LOW);
   
      delay(200);
      
      motorState = !motorState;
      
      digitalWrite(I1, motorState);
      digitalWrite(I2, !motorState);
      digitalWrite(I3, motorState);
      digitalWrite(I4, !motorState);
      
      analogWrite(E1, 153); // Run in half speed
      analogWrite(E2, 153); // Run in half speed
    }
}
