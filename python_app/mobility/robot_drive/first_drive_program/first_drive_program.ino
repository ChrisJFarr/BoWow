#include <Adafruit_MotorShield.h>
#include <Wire.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"
#include <stdlib.h>     /* abs */

// Create the Adafruit_MotorShiel object
Adafruit_MotorShield AFMS = Adafruit_MotorShield();
// Request the DC motor from the Adafruit_MotorShield
Adafruit_DCMotor *frontLeftMotor = AFMS.getMotor(1);
Adafruit_DCMotor *backLeftMotor = AFMS.getMotor(2);
Adafruit_DCMotor *frontRightMotor = AFMS.getMotor(3);
Adafruit_DCMotor *backRightMotor = AFMS.getMotor(4);

// Movement support/ communication
int incoming[4];
int travelSpeed = 0;
int travelDirection = 1;

void setup() {
  Serial.begin(9600); //start serial port
  // put your setup code here, to run once:
  // Call begin on the AFMS object
  AFMS.begin();
  // Set the default speed
  setLeftSpeed(0);
  setRightSpeed(0);

}

void loop() {

  // Fill incoming array
  fillIncoming();

  // Set travelSpeed with incoming[0] if there is a change
  if(incoming[0] != travelSpeed)
  {
    travelSpeed = incoming[0];
  }

  // Check for rotation, else set driving direction
  if(incoming[2]==0 && incoming[3]==2)
  {
    // If left = 0 and right = 2 then rotate left
    rotateLeft();
    setLeftSpeed(255);
    setRightSpeed(255);
  } else if(incoming[2]==2 && incoming[3]==0)
  {
    // If left = 2 and right = 0 then rotate right
    rotateRight();
    setLeftSpeed(255);
    setRightSpeed(255);
  } else 
  {
    // Set default travel speed for both sides
    setRightSpeed(travelSpeed);
    setLeftSpeed(travelSpeed);
    if(incoming[1] == 1)  // Set driving direction
    {
      driveForward();
    } else
    {
      driveBackward();
    }
  }
  
  if(incoming[2]==0 && incoming[3]==1)
  {
    // If left = 0 and right = 1 then add speed to right, take from left
    setRightSpeed(travelSpeed + 55);
    setLeftSpeed(0);
  } else if(incoming[2]==1 && incoming[3]==0)
  {
    // If left = 1 and right = 0 then add speed to left
    setRightSpeed(0);
    setLeftSpeed(travelSpeed + 55);
  } 
  delay(50);
}

void fillIncoming()
{
  // Fill incoming array with Serial.read()
  while(Serial.available() >= 4)
  {
    // fill array with loop
    for(int i = 0; i < 4; i++)
    {
      incoming[i] = Serial.read();
    }
  }
}


void rotateLeft()
{
  frontLeftMotor->run(BACKWARD);
  backLeftMotor->run(BACKWARD);
  backRightMotor->run(FORWARD);
  frontRightMotor->run(FORWARD);
}

void rotateRight()
{
  frontLeftMotor->run(FORWARD);
  backLeftMotor->run(FORWARD);
  backRightMotor->run(BACKWARD);
  frontRightMotor->run(BACKWARD);
}

void driveForward()
{
  frontLeftMotor->run(FORWARD);
  backLeftMotor->run(FORWARD);
  backRightMotor->run(FORWARD);
  frontRightMotor->run(FORWARD);
}

void driveBackward()
{
  frontLeftMotor->run(BACKWARD);
  backLeftMotor->run(BACKWARD);
  backRightMotor->run(BACKWARD);
  frontRightMotor->run(BACKWARD);
}

void stopDriving()
{
  frontLeftMotor->run(RELEASE);
  backLeftMotor->run(RELEASE);
  frontRightMotor->run(RELEASE);
  backRightMotor->run(RELEASE);
}

void setLeftSpeed(int newSpeed)
{
  frontLeftMotor->setSpeed(newSpeed);
  backLeftMotor->setSpeed(newSpeed);
}

void setRightSpeed(int newSpeed)
{
  frontRightMotor->setSpeed(newSpeed);
  backRightMotor->setSpeed(newSpeed);
}

