import serial
import time
import numpy as np

def main():
    # Configure the serial connection
    arduino_port = 'COM3'
    baud_rate = 9600       
    timeout = 1            
    red, green, blue = 0, 0, 0
    reading = True
    reds = []
    blues = []
    greens = []

    try:
        # Open the serial connection
        with serial.Serial(arduino_port, baud_rate, timeout=timeout) as ser:
            print(f"Connected to Arduino on {arduino_port} at {baud_rate} baud.")
            
            # while True:
                # Send data to Arduino
            message = input("Enter a message to send to Arduino (or 'exit' to quit): ")
            if message == 'start':
                for i in range(35):
                    reading = True
                    ser.write(message.encode('utf-8'))
                    while reading:
                        if ser.in_waiting > 0:
                            response = ser.readline().decode('utf-8').strip()
                            print(f"Arduino says: {response}")
                            if 'R' in response:
                                red = float(response.split('R : ')[1])
                            elif 'G' in response:
                                green = float(response.split('G : ')[1])
                            elif 'B' in response:
                                blue = float(response.split('B : ')[1])
                        
                        if blue > 0:
                            print(f"RGB Values - R: {red}, G: {green}, B: {blue}")
                            reds.append(red)
                            blues.append(blue)
                            greens.append(green)
                            blue = 0
                            reading = False
                            time.sleep(0.01)
            else:
                reading = False
                # if message.lower() == 'exit':
                #     print("Exiting...")
                #     break
                # print(f"Sent: {message}")

                # Read response from Arduino
                # time.sleep(0.1)  # Give Arduino time to respond
            

            print(len(reds[4:]))
            redMean, blueMean, greenMean = np.mean(reds[4:]), np.mean(blues[4:]), np.mean(greens[4:])
            print(f"Average RGB Values - R: {redMean}, G: {greenMean}, B: {blueMean}")

    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")

if __name__ == "__main__":
    main()