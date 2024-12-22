# Kafka KRaft Single Node Setup on Ubuntu

This repository provides a step-by-step guide for setting up a single-node Kafka instance with KRaft mode on an Ubuntu system. KRaft (Kafka Raft) eliminates the dependency on Zookeeper, making it simpler to deploy and manage.

## Prerequisites
- Ubuntu OS (20.04 or later recommended)
- Basic knowledge of Linux commands
- A non-root user with `sudo` privileges

---

## Step 1: Update the System
Ensure your system has the latest updates:
```bash
sudo apt update
```

## Step 2: Install Java
Kafka requires Java to run. Install OpenJDK 11:
```bash
sudo apt install openjdk-11-jdk
java -version
```
Verify the installation by checking the Java version.

## Step 3: Download and Extract Kafka
Download Kafka version 3.0.0 from the Apache archive:
```bash
wget https://archive.apache.org/dist/kafka/3.0.0/kafka_2.13-3.0.0.tgz
tar -xzf kafka_2.13-3.0.0.tgz
```
Extracted Kafka will be in the directory `kafka_2.13-3.0.0`.

## Step 4: Configure and Start Kafka
### Generate a UUID
Run the following command to generate a unique ID for Kafka storage:
```bash
~/kafka_2.13-3.0.0/bin/kafka-storage.sh random-uuid
```

### Format the Storage Directory
Replace `<UUID>` with the generated UUID:
```bash
~/kafka_2.13-3.0.0/bin/kafka-storage.sh format -t <UUID> -c ~/kafka_2.13-3.0.0/config/kraft/server.properties
```

### Start Kafka in KRaft Mode
Run the Kafka server as a daemon:
```bash
~/kafka_2.13-3.0.0/bin/kafka-server-start.sh -daemon ~/kafka_2.13-3.0.0/config/kraft/server.properties
```

### Stop Kafka
To stop the Kafka server:
```bash
~/kafka_2.13-3.0.0/bin/kafka-server-stop.sh
```

## Step 5: Create and Manage Topics
### Create a Topic
```bash
~/kafka_2.13-3.0.0/bin/kafka-topics.sh --create --topic Test1 --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092
```

### Describe the Topic
```bash
~/kafka_2.13-3.0.0/bin/kafka-topics.sh --describe --topic Test1 --bootstrap-server localhost:9092
```

### Produce Messages
Send messages to the topic:
```bash
~/kafka_2.13-3.0.0/bin/kafka-console-producer.sh --topic Test1 --bootstrap-server localhost:9092
```

### Consume Messages
Consume messages from the topic:
```bash
~/kafka_2.13-3.0.0/bin/kafka-console-consumer.sh --topic Test1 --from-beginning --bootstrap-server localhost:9092
```

## Step 6: Configure Kafka as a Systemd Service
To simplify management, configure Kafka as a systemd service.

### Create the Kafka Service File
Create and edit the service file:
```bash
sudo nano /etc/systemd/system/kafka.service
```

Add the following content:
```plaintext
[Unit]
Description=Apache Kafka
After=network.target

[Service]
User=ubuntu
Group=ubuntu
ExecStart=/home/ubuntu/kafka_2.13-3.0.0/bin/kafka-server-start.sh /home/ubuntu/kafka_2.13-3.0.0/config/kraft/server.properties
ExecStop=/home/ubuntu/kafka_2.13-3.0.0/bin/kafka-server-stop.sh
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```

### Enable and Start the Kafka Service
Reload systemd and enable Kafka to start on boot:
```bash
sudo systemctl daemon-reload
sudo systemctl enable kafka.service
sudo systemctl start kafka.service
```

### Verify the Kafka Service
Check the service status:
```bash
sudo systemctl status kafka.service
```

---

## Next Steps
You now have a single-node Kafka instance running in KRaft mode. To explore further:
- Learn about **Kafka Streams** for stream processing.
- Set up a **multi-node Kafka cluster**.
- Integrate Kafka with other systems like Elasticsearch, Spark, or Flink.

For questions or suggestions, feel free to raise an issue or contact me!

---

### License
This guide is open-source and available under the MIT License.
