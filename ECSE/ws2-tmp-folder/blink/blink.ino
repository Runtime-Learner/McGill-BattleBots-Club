#define ledPin 13

void setup() {
  pinMode(ledPin, OUTPUT); //led is an output
}

void loop() {
  //set pin to have 5V -> LED on
  digitalWrite(ledPin, HIGH);
  delay(1000);
  //set pin to have 0V -> LED off
  digitalWrite(ledPin, LOW);
  delay(1000);
}
