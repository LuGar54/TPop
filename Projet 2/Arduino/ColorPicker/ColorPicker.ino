int analogPin = A0;

int blueLedPin = 6;
int redLedPin = 7;
int greenLedPin = 8;

int switchPin = 2;
int switchValue = 1;

bool acquiring = false;
bool switched = false;

const int ACQUISITION_TIME = 3000;
const int LED_UP_TIME = 250;

int iterationCounter = 0;

float currentColorMean = 0;

float blueMean = 0;
float redMean = 0;
float greenMean = 0;

int currentColor = 0;

float calibrationRed = 20;
float calibrationGreen = 150;
float calibrationBlue = 200;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  pinMode(blueLedPin, OUTPUT);
  pinMode(redLedPin, OUTPUT);
  pinMode(greenLedPin, OUTPUT);

  pinMode(switchPin, INPUT_PULLUP);
}

void loop() {
  // put your main code here, to run repeatedly:
  switchValue = digitalRead(switchPin);

  // Serial.println(acquiring);

  if (Serial.available() > 0) {
    String message = Serial.readStringUntil('\n');
    if (message == "start") {
      startAcquisition();
    }
  }

  // Serial.println(switchValue);

  if (acquiring) {
    if (currentColor == 0) {
      redMean = measureColor(redLedPin);
    }
    else if (currentColor == 1) {
      greenMean = measureColor(greenLedPin);
    }
    else if (currentColor == 2) {
      blueMean = measureColor(blueLedPin);
    }
    else {
      acquiring = false;
      currentColor = 0;
      
      Serial.print("R : ");
      // Serial.println(redMean/calibrationRed);
      Serial.println(redMean);

      Serial.print("G : ");
      // Serial.println(greenMean/calibrationGreen);
      Serial.println(greenMean);

      Serial.print("B : ");
      // Serial.println(blueMean/calibrationBlue);
      Serial.println(blueMean);
      blueMean = 0;
      redMean = 0;
      greenMean = 0;
      //Serial.println(currentColorMean);
    }
  }
}

void startAcquisition() {
  acquiring = true;
}


float measureColor(int colorPin) {
  analogWrite(colorPin, 255);
  // Serial.print(blueTime);
  // Serial.print("   ");

  if (iterationCounter > LED_UP_TIME) {
    currentColorMean += 1024-analogRead(analogPin);
  }

  iterationCounter++;

  if (iterationCounter >= ACQUISITION_TIME) {
    // Serial.println(currentColorMean/(iterationCounter-LED_UP_TIME));
    analogWrite(colorPin, 0);
    // acquiring = false;
    iterationCounter = 0;
    // blueMean = 0;
    currentColor++;
    float tempAnswer = currentColorMean / (ACQUISITION_TIME - LED_UP_TIME);
    currentColorMean = 0;
    return tempAnswer;
  }
  return 0;
}
