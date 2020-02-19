#define inputPin A0

void setup() {
  pinMode(inputPin, INPUT_PULLUP); //A0 will standby at 5V
  Serial.begin(9600);
}

void loop() {
  Serial.print(analogRead(inputPin)); //write the value of the input pin to the computer
  Serial.print("\n");
  delay(75); //pause to reduce sampling rate
}
