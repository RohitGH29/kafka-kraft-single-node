# kafka-kraft-single-node

# Update the OS
1. sudo apt update

# Install JAVA 
1. sudo apt install openjdk-11-jdk
2. java -version

# Download Kakfa 
1. wget https://archive.apache.org/dist/kafka/3.0.0/kafka_2.13-3.0.0.tgz
2. tar -xzf kafka_2.13-3.0.0.tgz 
3. ~/kafka_2.13-3.0.0/bin/kafka-storage.sh random-uuid
4. ~/kafka_2.13-3.0.0/bin/kafka-storage.sh format -t J3OpYYJVTXyN9OiIq37ILw -c ~/kafka_2.13-3.0.0/config/kraft/server.properties            (Replace the uuid)
 output: Formatting /tmp/kraft-combined-logs  
5. ~/kafka_2.13-3.0.0/bin/kafka-server-start.sh -daemon ~/kafka_2.13-3.0.0/config/kraft/server.properties 
6. ~/kafka_2.13-3.0.0/bin/kafka-server-stop.sh  (To stop kafka)
7. ~/kafka_2.13-3.0.0/bin/kafka-topics.sh --create --topic Test1 --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092
8. ~/kafka_2.13-3.0.0/bin/kafka-topics.sh --describe --topic Test1 --bootstrap-server localhost:9092
9. ~/kafka_2.13-3.0.0/bin/kafka-console-producer.sh --topic Test1 --bootstrap-server localhost:9092
10. ~/kafka_2.13-3.0.0/bin/kafka-console-consumer.sh --topic Test1 --from-beginning --bootstrap-server localhost:9092

# Steps to Set Up Kafka as a Systemd Service:
1. sudo nano /etc/systemd/system/kafka.service     //check kafka.service file
2. sudo systemctl daemon-reload
3. sudo systemctl enable kafka.service
4. sudo systemctl start kafka.service
5. sudo systemctl status kafka.service
