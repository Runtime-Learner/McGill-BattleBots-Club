
#define inputPin A0

void setup() {
  pinMode(inputPin, INPUT_PULLUP); //set pin A0 to be an input pin.
                                  //and set it to standby at 5V
                                  
  Serial.begin(9600); //begin a serial connection with the computer
}

void loop() {
  Serial.print(analogRead(inputPin)); //write the value of the input pin to the computer
  Serial.print("\n");
  delay(75); //pause to reduce the sampling rate
}
