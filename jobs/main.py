import os
from confluent_kafka import SerializingProducer
import simplejson as json

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
