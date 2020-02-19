#define pin 2     //pin on which the button will be connected
#define ledPin 9 //LED pin. is onboard the arduino and does not have to be connected manually
#define ledTimer 13 //LED that will be running with a timer

int ledState;     //variable used to store whether or not the LED is currently turned on

void setup() {
  
  pinMode(pin, INPUT_PULLUP); //button pin is input. Set it to be 5V standby
  pinMode(ledPin, OUTPUT);    //led pin is output
  pinMode(ledTimer, OUTPUT); //led pin is output
  //led is turned off
  ledState = LOW;
  digitalWrite(ledPin, ledState);
  digitalWrite(ledTimer, LOW);
}

void loop() {
  //check to see if the button pin is not the same state as the LED.
  if (digitalRead(pin) != ledState){
    
    ledState = digitalRead(pin);    //set ledState to be the same as the button state
    digitalWrite(ledPin, !ledState); //write the new LED state to the led pin
    delay(50);
  }


  //turn other LED on/off for a certain amount of time
  int delayTime = 1000;
  digitalWrite(ledTimer, HIGH);
  delay(delayTime);
  digitalWrite(ledTimer, LOW);
  delay(delayTime);
}
