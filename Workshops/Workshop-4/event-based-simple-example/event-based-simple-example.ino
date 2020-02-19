#define pin 2     //pin on which the button will be connected
#define ledPin 9 //LED pin. is onboard the arduino and does not have to be connected manually
#define ledTimer 13 //LED that will be running with a timer

int buttonLedState = LOW;     //store state of button LED
int timerLedState = LOW;      //store state of timer LED

//store last time   events ran
unsigned long buttonLastTime = 0;    
unsigned long timerLastTime = 0;   

//store how long to wait before rerunning event
unsigned int buttonEventDelay = 50;  
unsigned int timerEventDelay = 100;

void setup() {
  pinMode(pin, INPUT_PULLUP); //button pin is input. Set it to be 5V standby
  pinMode(ledPin, OUTPUT);    //led pin is output
  pinMode(ledTimer, OUTPUT); //led pin is output
  
  //LEDs are turned off
  digitalWrite(ledPin, buttonLedState);
  digitalWrite(ledTimer, timerLedState);
}

void loop() {
  unsigned long curTime = millis(); //get the current time, in milliseconds
  ButtonEvent(curTime);
  timedLedEvent(curTime);
}

void ButtonEvent(unsigned long currentTime){
  //check to see if enough time has passed to redo event
  if (currentTime - buttonLastTime < buttonEventDelay){
    return;
  }

  //run event if that is the case
  //check to see if the button pin is not the same state as the LED.
  if (digitalRead(pin) != buttonLedState){
    
    buttonLedState = digitalRead(pin);    //set ledState to be the same as the button state
    digitalWrite(ledPin, !buttonLedState); //write the new LED state to the led pin
  }

  buttonLastTime = currentTime; //set the current time to be the last time the event has been run
}

void timedLedEvent(unsigned long currentTime){
  //check to see if enough time has passed to redo event
  if (currentTime - timerLastTime < timerEventDelay){
    return;
  }
  
  //run event if that is the case
  timerLedState = !timerLedState; //switch the state of timer LED
  digitalWrite(ledTimer, timerLedState);

  timerLastTime = currentTime; //set the current time to be the last time the event has been run
}
