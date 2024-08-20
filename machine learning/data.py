import csv
import numpy as np

def generate_sensor_data(speed, acceleration, steering_angle):
    """
    Generate sensor data based on given speed, acceleration, and steering angle
    """
    # Determine whether driving forward or backward
    if speed > 0:
        driving_state = 'Forward'
    elif speed < 0:
        driving_state = 'Backward'
    else:
        driving_state = 'Stopped'
    
    # Determine rapid acceleration or deceleration
    if acceleration > 3:
        driving_condition = 'Rapid acceleration'
    elif acceleration < -3:
        driving_condition = 'Rapid deceleration'
    else:
        driving_condition = 'Normal'
    
    # Determine right turn or left turn
    if steering_angle > 0:
        turning_direction = 'Right turn'
    elif steering_angle < 0:
        turning_direction = 'Left turn'
    else:
        turning_direction = 'Straight'
    
    # Generate sensor data
    sensor_data = {
        'Speed': speed,
        'Acceleration': acceleration,
        'Steering angle': steering_angle,
        'Driving state': driving_state,
        'Driving condition': driving_condition,
        'Turning direction': turning_direction
    }
    return sensor_data

sensor_data_list = []

# Generate 100 sensor data
for _ in range(100):
    # Generate random values for speed, acceleration, and steering angle
    speed = np.random.uniform(-20, 20)  # Speed between -20 and 20
    acceleration = np.random.uniform(-10, 10)  # Acceleration between -10 and 10
    steering_angle = np.random.uniform(-np.pi / 6, np.pi / 6)  # Steering angle between -30 degrees and 30 degrees
    
    # Generate sensor data with the generated values
    sensor_data = generate_sensor_data(speed, acceleration, steering_angle)
    
    # Add sensor data to the list
    sensor_data_list.append(sensor_data)

# Write data to CSV file
with open('sensor_data.csv', mode='w', newline='') as file:
    fieldnames = ['Speed', 'Acceleration', 'Steering angle', 'Driving state', 'Driving condition', 'Turning direction']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Write header
    writer.writeheader()
    
    # Write sensor data
    for data in sensor_data_list:
        writer.writerow(data)
