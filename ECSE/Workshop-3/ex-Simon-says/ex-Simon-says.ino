// the setup function runs once when you press reset or power the board

void(* resetFunc) (void) = 0; //declare reset function @ address 0


#define NUM_ROW 4
#define NUM_COL 5

#define ROW_S 3
#define COL_S ROW_S + NUM_ROW

#define ROW1 ROW_S
#define ROW2 ROW_S + 1
#define ROW3 ROW_S + 2
#define ROW4 ROW_S + 3

#define COL1 COL_S
#define COL2 COL_S + 1
#define COL3 COL_S + 2
#define COL4 COL_S + 3
#define COL5 COL_S + 4


#define BUZZER 12
// #define false 0
// #define true 1

short lives = 3;
short playerTurn = false;

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(ROW1, OUTPUT);
  pinMode(ROW2, OUTPUT);
  pinMode(ROW3, OUTPUT);
  pinMode(ROW4, OUTPUT);
  pinMode(COL1, OUTPUT);
  pinMode(COL2, OUTPUT);
  pinMode(COL3, OUTPUT);
  pinMode(COL4, OUTPUT);
  pinMode(COL5, OUTPUT);
  
  digitalWrite(COL1, HIGH);
  digitalWrite(COL2, HIGH);
  digitalWrite(COL3, HIGH);
  digitalWrite(COL4, HIGH);
  digitalWrite(COL5, HIGH);

//BUTTONS
  pinMode(A0, INPUT_PULLUP); //first row of buttons
  pinMode(A1, INPUT_PULLUP); //first row of buttons
  pinMode(A2, INPUT_PULLUP); //first row of buttons
  pinMode(A3, INPUT_PULLUP); //first row of buttons
  
  
//buzzer
    pinMode(BUZZER, OUTPUT);
    digitalWrite(BUZZER, HIGH);
  
  
  ///TOASTING PorePOSES
     //2D light matrix control
//  for(short x = 0; x<5; x++){
//  for(short y = 0; y<4; y++){
//     turnOn(x, y);
//     delay(150);
//     disableGrounds();
//     }
//  }
  
//     for (int i = 0; i < NUM_ROW; i++)
//     {
//         lightRow(i, 0, NUM_COL);
//         delay(1000);
//         disableGrounds();
//         delay(1000);
//     }
    
//   for (int i = 0; i < NUM_COL; i++)
//     {
//         lightCol(i, 0, NUM_ROW);
//         delay(1000);
//         disableGrounds();
//         delay(1000);
//     }
    
  animation1(200); 
  
  randomSeed(analogRead(A7));
  short rnd = 0;



  //INTERRUPT 
  pinMode(2, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(2), resetFunc, CHANGE);

}

// The loop function runs over and over again forever
void loop() {
    lives = 3;
    short l = 5000;
    short pattern[l] = {0};
    
    //allOn();
    //btn();
    for(int rnd = 1; rnd<=l; rnd++){
        nextLight(pattern, rnd, 16);
        runRound(pattern, rnd, 16);
        drawHealth_3(100);
        disableGrounds();
        
        short current_pressed = -1;
        short compare_to = 0;
        
        while(compare_to <rnd){
            playerTurn = true;
            drawHealth_2();
            disableGrounds();
            short pressed = btn();
            if (pressed != current_pressed)
            {
                current_pressed = pressed;
                if (pattern[compare_to] == pressed)
                {
                    
                    compare_to++;
                    continue;
                }    
                else if (pressed != -1)
                {
                    playerTurn = false;
                    lives--;
                    allOn();
                    if (lives <= 0)
                        resetFunc();
                    drawHealth_3(500);
                    // delay(500);
                    
                    runRound(pattern, rnd, 16);
                    compare_to = 0;
                    // current_pressed = -1;
                    continue;
                }
                else
                {
                    current_pressed = -1;
                    continue;
                }
            current_pressed = pressed;                
            }
        }
        playerTurn = false;
        while(btn() != -1)
        {
            drawHealth_3(2);
            disableGrounds();
        }
        drawHealth_3(500);
    }
}

void stahp(int time, short current){
    for(int x = 0; x<time; x++){
        drawHealth_2();
        // delay(1);
        disableGrounds();
        turnOn_1d(current);
        delay(1);
        disableGrounds();
    }
    turnOn_1d(current);
}

// void delay(int time, short currentL){
//     if (currentL != -1){
//         for (int i=0; i <time; i++){
//         drawHealth_2();
//         delay(1);
//         }       
//     }
//     else
//     {
//         for (int i=0; i <time; i++){
//         drawHealth(currentL);
//         delay(1);
//         }     
//     }
// }

void drawHealth_2(){
    disableGrounds();
    lightCol(4, 4-lives, NUM_ROW);
    if playerTurn
        turnOn(NUM_ROW, NUM_COL);
    // disableGrounds();
}

void drawHealth_3(short t){
    for(int i = 0; i < t; i++){
        disableGrounds();
        delay(1);
        lightCol(4, 4-lives, NUM_ROW);   
        if playerTurn
            turnOn(NUM_ROW, NUM_COL);
    }

    // disableGrounds();
}

void drawHealth(short currentLightOn){
    disableGrounds();
    lightCol(4, 4-lives, NUM_ROW);
    if playerTurn
        turnOn(NUM_ROW, NUM_COL);
    disableGrounds();
    turnOn_1d(currentLightOn);
    // delay(10);
    //disableGrounds();   
}

// Turns on all lights
void allOn() {
    for (int i = 0; i < 3; i++)
    {
    digitalWrite(COL1, LOW);
    digitalWrite(COL2, LOW);
    digitalWrite(COL3, LOW);
    digitalWrite(COL4, LOW);
    digitalWrite(COL5, LOW);
    digitalWrite(ROW1, HIGH);
    digitalWrite(ROW2, HIGH);
    digitalWrite(ROW3, HIGH);
    digitalWrite(ROW4, HIGH);
    digitalWrite(BUZZER, LOW);   
    delay(100);
    disableGrounds();
    digitalWrite(BUZZER, HIGH);   
    delay(100);
    }

}



//   //1D light matrix control alternative
//   for(short x = 0; x<16; x++){
//     turnOn_1d(x);
//     delay(250, x);
//     disableGrounds();
//     btn();
//   }

//    //2D light matrix control
//  for(short x = 0; x<4; x++){
//  for(short y = 0; y<4; y++){
//    turnOn(x, y);
//    delay(250, x*4 + y);
//    disableGrounds();
//    }
//  }

void nextLight(short arr[], short rnd, short size){
    
    arr[rnd] = random(0, size);
}

void runRound(short arr[], short rnd, short size){
    
    for(short i=0; i<rnd; i++){
        turnOn_1d(arr[i]);
        stahp(500, arr[i]);
        // delay(500);
        disableGrounds();
        //btn();
        drawHealth_3(50);
        disableGrounds();
    }
}

int btn(){

  //get button input.
  // read the input on analog pin 0:
  int sV0 = analogRead(A0);
  int sV1 = analogRead(A1);
  int sV2 = analogRead(A2);
  int sV3 = analogRead(A3);
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float v0 = sV0 * (5.0 / 1023.0);
  float v1 = sV1 * (5.0 / 1023.0);
  float v2 = sV2 * (5.0 / 1023.0);
  float v3 = sV3 * (5.0 / 1023.0);
  
  if (v0 > 4.6 && v1 > 4.6 && v2 > 4.6 && v3 > 4.6)
    return -1;
    
  //1st row
  if (v0 < 3.63)
  {
    turnOn(0, 0);
    delay(1);
    return 0;
  }
  else if (v0 < 3.85)
    {
        turnOn(1, 0);
        delay(1);
        return 4;
    }
  else if (v0 <  4.05)
    {
        turnOn(2, 0);
        delay(1);
        return 8;
    }
  else if (v0 < 4.4)
    {
        turnOn(3, 0);
        delay(1);
        return 12;
    }
    
    //2st row
  if (v1 < 3.63)
    {
        turnOn(0, 1);
        delay(1);
        return 1;
    }
  else if (v1 < 3.85)
    {
        turnOn(1, 1);
        delay(1);
        return 5;
    }
  else if (v1 <  4.05)
    {
        turnOn(2, 1);
        delay(1);
        return 9;
    }
  else if (v1 < 4.4)
    {
        turnOn(3, 1);
        delay(1);
        return 13;
    }
    
      //3st row
  if (v2 < 3.63)
    {
        turnOn(0, 2);
        delay(1);
        return 2;
    }
  else if (v2 < 3.85)
    {
        turnOn(1, 2);
        delay(1);
        return 6;
    }
  else if (v2 <  4.05)
    {
        turnOn(2, 2);
        delay(1);
        return 10;
    }
  else if (v2 < 4.4)
    {
        turnOn(3, 2);
        delay(1);
        return 14;
    }
    
      //4st row
  if (v3 < 3.63)
    {
        turnOn(0, 3);
        delay(1);
        return 3;
    }
  else if (v3 < 3.85)
    {
        turnOn(1, 3);
        delay(1);
        return 7;
    }
  else if (v3 <  4.05)
    {
        turnOn(2, 3);
        delay(1);
        return 11;
    }
  else if (v3 < 4.4)
    {
        turnOn(3, 3);
        delay(1);
        return 15;
    }
    
  disableGrounds();
}


void lightCol(short col, short start, short upto) {
    for(short x = upto-start; x >0; x--)
      digitalWrite(ROW_S+upto-x, HIGH);
    digitalWrite(col + COL_S, LOW);
}



void lightRow(short row, short start, short upto) {

    for(short x = upto-start; x >0; x--)
      digitalWrite(COL_S +upto-x, LOW);
    digitalWrite(row + ROW_S, HIGH);
}

void disableGrounds(){
    digitalWrite(COL1, HIGH);
    digitalWrite(COL2, HIGH);
    digitalWrite(COL3, HIGH);
    digitalWrite(COL4, HIGH);
    digitalWrite(COL5, HIGH);
    digitalWrite(ROW1, LOW);
    digitalWrite(ROW2, LOW);
    digitalWrite(ROW3, LOW);
    digitalWrite(ROW4, LOW);
  }

void turnOn_1d(short x){
  turnOn(x/4, x%4);
  
  }

void turnOn(short x, short y){
  digitalWrite(x + COL_S, LOW);
  digitalWrite(y + ROW_S, HIGH);
  }

void animation1(int m) {  //m = milliseconds per step of animation
    lightRow(1, 1, 3);
  lightRow(2, 1, 3);
  delay(m);
  disableGrounds();

  for (unsigned short i = 0; i < m/5; i++)
  for (short q = 0; q < 4; q+=3)
  {
    lightRow(q, 1, 3);
    delay(1);     
    disableGrounds(); 
    lightCol(q, 1, 3);
    delay(1);
    disableGrounds();
  }
  disableGrounds();
  
  for (unsigned short i = 0; i < m/5; i++)
  for (short q = 0; q < 4; q+=3)
  {
    turnOn(q, 0);
    turnOn(q, 3);
    delay(1);     
    disableGrounds(); 
    turnOn(0, q);
    turnOn(3, q);
    delay(1);
    disableGrounds();
  }

  disableGrounds();
  delay(m);
}
