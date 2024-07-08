import os
from confluent_kafka import SerializingProducer
import simplejson as json
import random
from datetime import datetime, timedelta
import uuid

KOLKATA_COORDINATES = {"latitude": 22.5744, "longitude": 88.3629}
DELHI_COORDINATES = {"latitude": 28.7041, "longitude": 77.1025}

# calculate movement inc


LATITUDE_INCREMENT = (
    DELHI_COORDINATES['latitude'] - KOLKATA_COORDINATES['latitude'])/100
LONGITUDE_INCREMENT = (
    DELHI_COORDINATES['longitude'] - KOLKATA_COORDINATES['longitude'])/100

# environment var for config

KAFKA_BOOTSTRAP_SERVERS = os.getenv(
    'KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
VEHICLE_TOPIC = os.getenv('VEHICLE_TOPIC', 'vehicle_data')
GPS_TOPIC = os.getenv('GPS_TOPIC', 'gps_data')
TRAFFIC_TOPIC = os.getenv('TRAFFIC_TOPIC', 'traffic_data')
WEATHER_TOPIC = os.getenv('WEATHER_TOPIC', 'weather_data')
EMERGENCY_TOPIC = os.getenv('EMERGENCY_TOPIC', 'emergency_data')

start_time = datetime.now()
start_location = KOLKATA_COORDINATES.copy()


def get_next_time():
    global start_time
    start_time += timedelta(seconds=random.randint(30, 60))
    return start_time


def simulate_vehicle_movement():
    global start_location

    start_location['latitude'] += LATITUDE_INCREMENT
    start_location['longitude'] += LONGITUDE_INCREMENT

    start_location['latitude'] += random.uniform(-0.0005, 0.0005)
    start_location['longitude'] += random.uniform(-0.0005, 0.0005)

    return start_location


def generate_vehicle_data(device_id):
    location = simulate_vehicle_movement()
    return {
        'id': uuid.uuid4(),
        'deviceId': device_id,
        'timestamp': get_next_time().isoformat(),
        'location': (location['latitude'], location['longitude']),
        'speed': random.uniform(10, 40),
        'make': 'BMW',
        'model': 'C500',
        'year': 2024,
        'fueltype': 'Hybrid'

    }


def simulate_journey(producer, device_id):
    while True:
        vehicle_data = generate_vehicle_data(device_id)
        gps_data = generate_gps_data(device_id, vehicle_data['timestamp'])

        break


if __name__ == "__main__":
    producer_config = {
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
        'error_cb': lambda err: print(f'Kafka error: {err}')
    }

    producer = SerializingProducer(producer_config)

    try:
        simulate_journey(producer, 'Vehicle-Ferris-2341')

    except KeyboardInterrupt:
        print('Simulation ended by the user')
    except Exception as e:
        print(f'Unexpected Error occurred: {e}')
