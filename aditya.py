import serial
import time

# Initialize serial connection (change the port name as per your setup)
ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # Wait for the serial connection to initialize

def control_water_pump(soil_moisture):
    # Threshold for soil moisture
    moisture_threshold = 300
    if soil_moisture < moisture_threshold:
        print("Turning on the water pump.")
        ser.write(b'1')  # Sending signal to Arduino to turn on the relay
    else:
        print("Turning off the water pump.")
        ser.write(b'0')  # Sending signal to Arduino to turn off the relay

while True:
    try:
        # Read data from serial
        data = ser.readline().decode().strip()
        if data:
            print(data)
            # Parse the data
            parts = data.split(',')
            humidity = float(parts[0].split(': ')[1].strip(' %'))
            temperature = float(parts[1].split(': ')[1].strip(' *C'))
            soil_moisture = int(parts[2].split(': ')[1])

            # Control the water pump based on soil moisture
            control_water_pump(soil_moisture)

        time.sleep(2)  # Wait before reading again

    except Exception as e:
        print(f"Error: {e}")

ser.close()