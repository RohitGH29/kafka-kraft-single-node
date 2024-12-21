from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import KafkaException

# Kafka broker configuration
conf = {
    'bootstrap.servers': '13.51.171.40:9092',
}

# Create an AdminClient instance
admin_client = AdminClient(conf)

# Define the topic configuration
topic_name = 'Test2'
num_partitions = 1  # Number of partitions
replication_factor = 1  # Replication factor

# Create a NewTopic object
new_topic = NewTopic(
    topic_name,
    # num_partitions=num_partitions,
    # replication_factor=replication_factor
)

# Create the topic
try:
    fs = admin_client.create_topics([new_topic])
    for topic, f in fs.items():
        try:
            f.result()  # The result of the create_topics operation
            print(f"Topic '{topic}' created successfully.")
        except KafkaException as e:
            print(f"Failed to create topic '{topic}': {e}")
except KafkaException as e:
    print(f"Error during topic creation: {e}")
