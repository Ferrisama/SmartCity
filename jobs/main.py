import os
from confluent_kafka import SerializingProducer
import simplejson as json
import random
from datetime import datetime

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


def simulate_vehicle_movement():
    global start_location

    start_location['latitude'] += LATITUDE_INCREMENT
    start_location['longitude'] += LONGITUDE_INCREMENT


def generate_vehicle_data(device_id):
    location = simulate_vehicle_movement()


def simulate_journey(producer, device_id):
    while True:
        vehicle_data = generate_vehicle_data(device_id)


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
