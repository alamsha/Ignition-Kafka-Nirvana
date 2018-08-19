# Ignition-Kafka-Nirvana
Build Massively Scalable SCADA Projects

**Tested on Ubuntu 18.04**

**Step 1 --- Setup Kafka Broker:**
Follow this link. It's very easy to setup.
https://kafka.apache.org/quickstart

**Step 2 --- Generate and serve dynamic Ignition tags as JSON payload:**
Download and run the "Ignition-IOT-Nirvana" demo project from github.
https://github.com/alamsha/Ignition-IOT-Nirvana

You can check this Ignition forum link. 
https://forum.inductiveautomation.com/t/web-api-to-read-write-tags-json/19038/36

**Step 3 --- Publish and Subscribe the JSON payload to the Kafka Broker:**
1. To Publish JSON payload:
    cd kafka-pubsub/
    pip install kafka-python
    python3 kafka-producer.py
https://github.com/dpkp/kafka-python


2. To Subscribe JSON payload:
    cd kafka-pubsub/
    yarn yarn add no-kafka
https://github.com/oleksiyk/kafka


