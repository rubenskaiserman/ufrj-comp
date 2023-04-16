#include "Arduino.h"

// C++ code
//
const int GREEN = 8;
const int ORANGE = 7;
const int RED = 13;
void setup()
{
  pinMode(GREEN, OUTPUT);
  pinMode(ORANGE, OUTPUT);
  pinMode(RED, OUTPUT);
}

void loop()
{
  digitalWrite(GREEN, HIGH);
  delay(1000);
  digitalWrite(GREEN, LOW);
  delay(1000);
  digitalWrite(ORANGE, HIGH);
  delay(1000);
  digitalWrite(ORANGE, LOW);
  delay(1000);
  digitalWrite(RED, HIGH);
  delay(1000);
  digitalWrite(RED, LOW);
  delay(1000);
}