import random
import time

# Function to simulate reading the soil moisture level (0-100)
def read_soil_moisture():
    return random.randint(0, 100)  # Random value between 0 (dry) and 100 (wet)

# Function to simulate getting weather forecast data (0-100 for chance of rain)
def get_weather_forecast():
    return random.randint(0, 100)  # Chance of rain (0 = no rain, 100 = heavy rain)

# Function to turn the irrigation system on or off
def control_irrigation(on):
    if on:
        print("Irrigation ON: Watering the plants...")
    else:
        print("Irrigation OFF: No need to water the plants.")

# Main function to simulate the irrigation system
def smart_irrigation():
    soil_moisture = read_soil_moisture()
    weather_forecast = get_weather_forecast()

    print(f"Current Soil Moisture: {soil_moisture}%")
    print(f"Weather Forecast (Chance of Rain): {weather_forecast}%")

    # Decision logic to turn on irrigation
    if soil_moisture < 30 and weather_forecast < 50:
        control_irrigation(True)  # Water the plants if soil is dry and no rain expected
    elif soil_moisture > 70 or weather_forecast > 50:
        control_irrigation(False)  # Don't water if soil is wet or rain is likely
    else:
        print("Soil moisture is adequate. No irrigation needed.")
    
# Simulate the system running every 5 seconds (for example)
while True:
    smart_irrigation()
    time.sleep(5)  # Wait for 5 seconds before checking again
