# Kafka_python
Read realtime map data and displays on website using Kafka,Python,Flask and Leaflet 

I have saved the lat, long values of diff bus routes in json. Sending these data as Kafka Message to topic geodata_final.
Validating data on runtime on webpage created in Flask and leaflet using javascript.

Steps to test - 
Setup Kafka locally and run start zookeeper and kafka server. Commands given below.
1. Run app.py and validate map on http://127.0.0.1:5001/ 
2. Run busline1.py validate live marker on webpage
3. Run busline2.py and busline3.py to test the same.

##########################################################################################
Kafka Local Set up : 
Add System env Path : C:\tools\kafka_2.12-2.5.0\bin\windows
create data folder and subfolders for kafka and zookeeper
Set this newly created path to zookeeper.config and server.config (With Forward slashes) 
########################################################################################

kafka Commands:

To Start Zookeeper: cd to  C:\tools\kafka_2.12-2.5.0\bin\windows
zookeeper-server-start.bat ../../config/zookeeper.properties

To Start kafka server:  cd to  C:\tools\kafka_2.12-2.5.0\bin\windows
kafka-server-start.bat ../../config/server.properties

########################################################################################
Create Topic in kafka

kafka-topics.bat --zookeeper 0.0.0.0:2181  --topic test_topic --create --partitions 1 --replication-factor 1

kafka-topics.bat --zookeeper 0.0.0.0:2181  --topic test_topic --describe

#######################################################################################
Creating Producer and Consumer is done programatically, below commands to validate it manually.
Create Producer:
kafka-console-producer.bat --broker-list localhost:9092 --topic test_topic

Start Consumer console-producer
kafka-console-consumer.bat  --bootstrap-server localhost:9092 --topic test_topic  --from-beginning

Now Send messages from Producer and validate on Consumer console.

You are going great so far :)
