#include <Servo.h> //include the servo library

// Declare Variables
int incoming[3];
int xPos=90; //declare initial position of the servo
int yPos=175; //declare initial position of the servo
int xServoPin = 9; //declare pin for the servo
int yServoPin = 6; //declare pin for the servo
int servoDelay = 1; //delay to allow the servo to reach position;
Servo xServo; // create a servo object called myServo
Servo yServo; // create a servo object called myServo

// the setup function runs once when you press reset or power the board
void setup() {
  Serial.begin(9600); //start serial port
  pinMode(LED_BUILTIN, OUTPUT); // initialize digital pin LED_BUILTIN as an output.
  xServo.attach(xServoPin); //declare to which pin is the servo connected
  yServo.attach(yServoPin); //declare to which pin is the servo connected
}

// the loop function runs over and over again forever
void loop() {
  // Fill incoming array with Serial.read()
  while(Serial.available() >= 3){
  // fill array
  for(int i = 0; i < 3; i++){
    incoming[i] = Serial.read();
  }

  // Determine type of request and execute
  
  // Check for LED command
  if(incoming[0] >= 1){
      if(incoming[0]==2){
    digitalWrite(LED_BUILTIN, HIGH);
  }
  else{
    digitalWrite(LED_BUILTIN, LOW);
  }
  }
  
  // Check for position command
  if(incoming[1] >= 1){
    int newXPos = incoming[1];
    int newYPos = incoming[2];

    // Pan left/right

    while(newXPos > xPos){
      xServo.write(xPos); //write the position into the servo
      delay(servoDelay); //give time to the servo to reach the position
      xPos += 1;
    }

     while(newXPos < xPos){
      xServo.write(xPos); //write the position into the servo
      delay(servoDelay); //give time to the servo to reach the position
      xPos -= 1;
    }

    // Tilt up/down
    while(newYPos > yPos){
      yServo.write(yPos); //write the position into the servo
      delay(servoDelay); //give time to the servo to reach the position
      yPos += 1;
    }
    
    while(newYPos < yPos){
      yServo.write(yPos); //write the position into the servo
      delay(servoDelay); //give time to the servo to reach the position
      yPos -= 1;
    }
  }
  }
}





