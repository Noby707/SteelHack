#include<Servo.h>

Servo serv;

int trig = 6;

int echo = 7;

int th;

float distance;

long duration, cm;

void setup() {

  // put your setup code here, to run once:

 
Serial.begin(9600);
Serial.print('hey');
 
pinMode(trig, OUTPUT);

 
pinMode(echo, INPUT);

 
serv.attach(9);

  th=0;

 
serv.write(th);


}

void loop() {

  // put your main code here, to run repeatedly:

 


digitalWrite(trig, LOW);
  delayMicroseconds(5);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

pinMode(echo, INPUT);
duration = pulseIn(echo, HIGH);
distance = (duration/2) /29.1;
if(Serial.available()>0){
Serial.println(distance);
}



}
