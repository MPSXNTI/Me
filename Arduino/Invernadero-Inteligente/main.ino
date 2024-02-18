#include <LiquidCrystal_I2C.h>
#include <Servo.h>

// Pin
#define LedWhite 7
#define LedRed 6
#define LedYellow 5
#define LedBlue 4
#define Trig 11
#define Echo 12
#define SerMor 9
#define Piezo 8
#define SenH A1
#define SenF A0

// Variable
LiquidCrystal_I2C lcd(0x27, 16, 2);
Servo motor;
int humedad = 0;
int luminicidad = 0;
int tiempo = 0;
int distancia = 0;

void setup() {
  // Analog
  pinMode(SenH, INPUT);
  pinMode(SenF, INPUT);

  // Digital
  pinMode(Piezo, OUTPUT);
  pinMode(Trig, OUTPUT);
  pinMode(Echo, INPUT);
  motor.attach(SerMor);

  lcd.init();
  lcd.backlight();
  Serial.begin(9600);
}

void loop() {
  mainArduino();
  delay(1000);
}

void mainArduino() {}
