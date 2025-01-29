int sensorPin = A0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(9, INPUT);
  // pinMode(sensorPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int experience = digitalRead(9);
  Serial.print(experience);
  Serial.print(",");
  Serial.println(analogRead(sensorPin));
}
