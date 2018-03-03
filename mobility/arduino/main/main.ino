// Imports for RobotDrive
#include <Adafruit_MotorShield.h>
#include <Wire.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"
#include <stdlib.h>     /* abs */






// Receive colon delimited strings to connect directly to flask API
// TODO http://forum.arduino.cc/index.php?topic=175610.0
class RobotDrive;



RobotDrive *robotDrive;

// Message support
String drive;
String pan;
String tilt;

// Open console and type "test" to test? Think of test scripts

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);

}

void loop()
{
  delay(50);
  read();
}


void read()
{
  drive = Serial.readStringUntil(':');
  pan = Serial.readStringUntil(':');
  tilt = Serial.readStringUntil(':');
  Serial.print("drive: ");
  Serial.println(drive);
  Serial.print("pan: ");
  Serial.println(pan);
  Serial.print("tilt: ");
  Serial.println(tilt);
}


//digitalWrite(LED_BUILTIN, HIGH);
// digitalWrite(LED_BUILTIN, LOW);
class RobotDrive {

    int speed = 0;
    
    // Create the Adafruit_MotorShield object
    Adafruit_MotorShield AFMS = Adafruit_MotorShield();

    // Request the DC motor from the Adafruit_MotorShield
    Adafruit_DCMotor *frontLeftMotor = AFMS.getMotor(1);
    Adafruit_DCMotor *backLeftMotor = AFMS.getMotor(2);
    Adafruit_DCMotor *frontRightMotor = AFMS.getMotor(3);
    Adafruit_DCMotor *backRightMotor = AFMS.getMotor(4);

  public: void execute(String drive)
    {
      // f: forward, b: backward, l: left, r: right
      for(int i=0;i<drive.length();i++) 
      {
        switch(drive.charAt(i))
        {
          case 'f':
           break;
        }
        }
      };

    void rotateLeft()
    {
      // Set motor directions for a left rotation
      frontLeftMotor->run(BACKWARD);
      backLeftMotor->run(BACKWARD);
      backRightMotor->run(FORWARD);
      frontRightMotor->run(FORWARD);
    }

    void rotateRight()
    {
      // Set motor directions for a right rotation
      frontLeftMotor->run(FORWARD);
      backLeftMotor->run(FORWARD);
      backRightMotor->run(BACKWARD);
      frontRightMotor->run(BACKWARD);
    }

    void driveForward()
    {
      // Set motor directions for driving foward
      frontLeftMotor->run(FORWARD);
      backLeftMotor->run(FORWARD);
      backRightMotor->run(FORWARD);
      frontRightMotor->run(FORWARD);
    }

    void driveBackward()
    {
      // Set motor directions for driving backward
      frontLeftMotor->run(BACKWARD);
      backLeftMotor->run(BACKWARD);
      backRightMotor->run(BACKWARD);
      frontRightMotor->run(BACKWARD);
    }

    void stopLeft()
    {
      // Stop left side motors
      frontLeftMotor->run(RELEASE);
      backLeftMotor->run(RELEASE);
    }

    void stopRight()
    {
      // Stop right side motors
      frontRightMotor->run(RELEASE);
      backRightMotor->run(RELEASE);
    }

    void setLeftSpeed(int newSpeed)
    {
      // If newSpeed is 0, stop left side
      if (newSpeed == 0)
      {
        stopLeft();
      }
      // Set left side speeds to newSpeed
      frontLeftMotor->setSpeed(newSpeed);
      backLeftMotor->setSpeed(newSpeed);

    }

    void setRightSpeed(int newSpeed)
    {
      // If newSpeed is 0, stop right side
      if (newSpeed == 0)
      {
        stopRight();
      }
      // Set right side speeds to newSpeed
      frontRightMotor->setSpeed(newSpeed);
      backRightMotor->setSpeed(newSpeed);

    }
};




