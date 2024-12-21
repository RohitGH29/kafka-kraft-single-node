from confluent_kafka import Producer
import configparser

# Read configuration from client.properties file
config = configparser.ConfigParser()
config.read('client.properties')

# Callback function to confirm delivery
def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Define Kafka producer configuration
conf = {
    'bootstrap.servers': '51.20.60.5:9092',
}

# Create a Kafka producer
producer = Producer(conf)

# Produce a single message to the topic "Test1"
topic = "Test1"
message_key = "1"
message_value = "New 1"

try:
    # Produce the message
    producer.produce(topic, key=message_key, value=message_value, callback=delivery_report)
    
    # Poll to handle delivery reports (callbacks)
    producer.poll(0)

    # Wait for all messages to be delivered
    producer.flush()

except Exception as e:
    print(f"Failed to produce message: {e}")
