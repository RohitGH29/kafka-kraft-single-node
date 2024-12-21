from confluent_kafka import Consumer, KafkaException
import configparser

# Read configuration from client.properties file
config = configparser.ConfigParser()
config.read('client.properties')

# Define Kafka consumer configuration with auto commit settings
conf = {
    # 'bootstrap.servers': 'kafka-1.kafka-headless.kafka.svc.cluster.local:9092',
    'bootstrap.servers': '51.20.60.5:9092',
    'group.id': 'G1',         # Consumer group ID
}

# Create a Kafka consumer
consumer = Consumer(conf)

# Subscribe to the topic "A"
consumer.subscribe(['Test1'])

try:
    while True:
        # Poll for messages
        msg = consumer.poll(timeout=1.0)  # Adjust timeout as needed

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition
                continue
            else:
                # Other errors
                raise KafkaException(msg.error())

        # Process message
        print(f"Received message: {msg.value().decode('utf-8')}")

except KeyboardInterrupt:
    # Handle cleanup on exit
    pass
finally:
    # Close the consumer
    consumer.close()
