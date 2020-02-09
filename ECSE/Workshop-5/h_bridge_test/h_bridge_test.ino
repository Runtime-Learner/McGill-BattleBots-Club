#define E1 6  // Enable Pin for motor 1
#define E2 3  // Enable Pin for motor 2
 
#define I1 5  // Control pin 1 for motor 1
#define I2 9  // Control pin 2 for motor 1
#define I3 2  // Control pin 1 for motor 2
#define I4 4  // Control pin 2 for motor 2
 
void setup() {
 
    pinMode(E1, OUTPUT);
    pinMode(E2, OUTPUT);
 
    pinMode(I1, OUTPUT);
    pinMode(I2, OUTPUT);
    pinMode(I3, OUTPUT);
    pinMode(I4, OUTPUT);
}
 
void loop() {
 
    //analogWrite(E1, 153); // Run in half speed
    analogWrite(E1, 255); // Run in full speed
 
    digitalWrite(I1, HIGH);
    digitalWrite(I2, LOW);
    digitalWrite(I3, HIGH);
    digitalWrite(I4, LOW);
 
    delay(4000);
 
    // change direction
 
    digitalWrite(E1, LOW);
    digitalWrite(E2, LOW);
 
    delay(200);
 
    analogWrite(E2, 255);  // Run in full speed
    //analogWrite(E2, 153);  // Run in half speed
 
    digitalWrite(I1, LOW);
    digitalWrite(I2, HIGH);
    digitalWrite(I3, LOW);
    digitalWrite(I4, HIGH);
 
    delay(4000);

        // change direction
 
    digitalWrite(E1, LOW);
    digitalWrite(E2, LOW);
 
    delay(200);
}
