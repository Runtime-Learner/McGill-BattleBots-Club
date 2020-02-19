//define number of rows and columns of LEDs will be controlled
#define NUM_ROW 2
#define NUM_COL 3

//define the first digital pins to connect for rows and columns (pins are assigned sequentially)
#define ROW_S 3
#define COL_S ROW_S + NUM_ROW


//row pins
#define ROW1 ROW_S
#define ROW2 ROW_S + 1

//column pins
#define COL1 COL_S
#define COL2 COL_S + 1
#define COL3 COL_S + 2

void setup() {
  // initialize all pins that will be used to control our LED matrix as an output.
  pinMode(ROW1, OUTPUT);
  pinMode(ROW2, OUTPUT);
  
  pinMode(COL1, OUTPUT);
  pinMode(COL2, OUTPUT);
  pinMode(COL3, OUTPUT);

  //turn all the columns to HIGH to avoid having the LEDs turn on (no V difference between anode and cathode)
  digitalWrite(COL1, HIGH);
  digitalWrite(COL2, HIGH);
  digitalWrite(COL3, HIGH);
}

// The loop function runs over and over again forever
void loop() {
  //2D light matrix control
  for(short x = 0; x<NUM_COL; x++){
    for(short y = 0; y<NUM_ROW; y++){
       turnOn(x, y);
       delay(500);
       disableGrounds();
     }
  }
  
     for (int i = 0; i < NUM_ROW; i++)
   {
       lightRow(i, 0, NUM_COL);
       delay(500);
       disableGrounds();
   }
    
   for (int i = 0; i < NUM_COL; i++)
   {
       lightCol(i, 0, NUM_ROW);
       delay(500);
       disableGrounds();
   }
}

// Turns on all lights
void allOn() {
    for (int i = 0; i < 3; i++)
    {
    digitalWrite(COL1, LOW);
    digitalWrite(COL2, LOW);
    digitalWrite(COL3, LOW);

    digitalWrite(ROW1, HIGH);
    digitalWrite(ROW2, HIGH);
    delay(100);
    disableGrounds();  
    delay(100);
    }

}

//turns all lights on a column in the range [start, upto]
void lightCol(short col, short start, short upto) {
    for(short x = upto-start; x >0; x--)
      digitalWrite(ROW_S+upto-x, HIGH);
    digitalWrite(col + COL_S, LOW);
}


//turns all lights on a row in the range [start, upto]
void lightRow(short row, short start, short upto) {
    for(short x = upto-start; x >0; x--)
      digitalWrite(COL_S +upto-x, LOW);
    digitalWrite(row + ROW_S, HIGH);
}

//sets the negative terminals to have 5V and the positive terminals to have 0V
void disableGrounds(){
  //grounds are the COL
    digitalWrite(COL1, HIGH);
    digitalWrite(COL2, HIGH);
    digitalWrite(COL3, HIGH);
    
  //V+ are the ROWS
    digitalWrite(ROW1, LOW);
    digitalWrite(ROW2, LOW);
  }

//turn on a light based on its 1D coordinate
void turnOn_1d(short x){
  turnOn(x/NUM_ROW, x%NUM_ROW);
  
  }
  
//turn on a light based on its (col, row) coordinate
void turnOn(short x, short y){
  digitalWrite(x + COL_S, LOW);
  digitalWrite(y + ROW_S, HIGH);
  }
