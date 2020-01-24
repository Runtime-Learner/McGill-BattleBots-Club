#define pin 2
#define ledPin 13
int ledState;

void setup() {
  // put your setup code here, to run once:
  pinMode(pin, INPUT);
  pinMode(ledPin, OUTPUT);
  ledState = LOW;
  digitalWrite(ledPin, ledState);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(pin) != ledState){
    ledState = digitalRead(pin);
    digitalWrite(ledPin, ledState);
    delay(50);
  }
}
