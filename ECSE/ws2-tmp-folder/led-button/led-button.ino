#define ledPin 13
#define buttonPin 2

bool ledState = LOW;

void setup() {
  pinMode(ledPin, OUTPUT); //led is an output
  pinMode(buttonPin, INPUT_PULLUP);
  /*
   * INPUT -> pin is LOW. detects when a voltage is applied
   * INPUT_PULLUP -> pin is HIGH. detects ehen connected to GND
   */
}

void loop() {
  if (ledState != digitalRead(buttonPin))
  {
    ledState = !ledState;
    digitalWrite(ledPin, ledState);
  }
}
