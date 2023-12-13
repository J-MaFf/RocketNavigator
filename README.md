# RocketNavigator

## Requirements Report for Rocketry Data Tracking System 
 
This requirements report outlines the specifications for the development of a Rocketry Data Tracking System using a Raspberry Pi. The system's primary purpose is to collect, store, and transmit data from various sensors during rocket flights. The report will cover the basic feature set, user groups, their needs, and non-functional requirements. 

  
### Basic Feature Set

1. **Data Collection:** The system collects data from sensors, including speed, GPS, and other external sensors.
2. **Data Storage:** Collected data is stored in a database for later analysis.
3. **Real-time GPS Tracking:** The system continuously sends GPS coordinates to users during rocket flights.
4. **Reliability:** The system must be highly reliable to prevent data loss.
5. **Sensor Handling:** It should gracefully handle sensor failures, either by stopping data collection for disconnected sensors or inputting null values.
6. **Updatability:** The system's code should be well-documented and modular for easy adaptation to new hardware.


### Primary Workflow

1. Sensors continuously collect data during a rocket's flight.
2. Collected data is transmitted to the Raspberry Pi for storage.
3. GPS coordinates are sent in real-time to users for monitoring.
4. The system maintains reliability and handles sensor failures.
5. The code is designed for updatability and adaptability to new sensors and hardware.
 

### Scenarios:

 **Scenario 1:** Data Collection and Storage 
- Rocketry club launches a rocket. 
- Sensors collect data during the flight. 
- Data is transmitted to the Raspberry Pi. 
- The system stores the data in a database. 
  
 **Scenario 2:** Real-time GPS Tracking 
- The system continuously transmits GPS coordinates during a rocket's flight. 
- Users receive GPS data for real-time monitoring. 
- The rocketry club ensures successful rocket recovery based on GPS information. 
  

### User Groups and Their Needs 

 **1. Rocketry Club:** 
    - The rocketry club needs the system to function reliably, collect accurate data, and provide real-time GPS tracking for monitoring rockets. They also want an easily updatable system for incorporating new sensors. 
  
 **2. Campus Police:** 
    - Campus Police want the system to maintain safety during rocket tests and ensure compliance with legal regulations. They are interested in the integration of software with hardware to ensure proper operation. 
  
 **3. Users Receiving GPS Data:** 
    - Users receiving GPS data, likely members of the rocketry club, expect continuous and accurate GPS coordinates for real-time tracking, ensuring successful rocket recovery. 
  

### Non-Functional Requirements and Constraints 
  
 **1. Responsiveness:**
    The system must remain responsive throughout the entire rocket flight, ensuring real-time data transmission.

 **2. Data Accuracy:**
    Data collected and stored must be accurate, and the system should maintain proper data points to support post-flight analysis.

 **3. Continuous GPS Tracking:**
    The GPS system is critical and must operate without interruptions to avoid rocket loss.

 **4. Hardware Compatibility:**
    The system should be compatible with various sensors and easily adaptable to accommodate new hardware.

 **5. Reliability:**
    The system must be highly reliable to prevent data loss or system failures, as any failure may result in additional launch costs.

 **6. Handling Sensor Failures:**
    The system should handle sensor failures gracefully, either by stopping data collection for disconnected sensors or inputting null values.

 **7. Updatability:**
    The code should be well-documented and modular, making it easy for future users to add or modify sensors.


### Conclusion 
    This requirements report outlines the key features, user groups, and non-functional requirements for the Rocketry Data Tracking System. The system aims to provide reliable data collection, real-time GPS tracking, and adaptability to new hardware. Meeting the needs and constraints of the stakeholders is crucial for the successful development and deployment of the system. 

DRIVE: https://drive.google.com/drive/folders/1q5S4ulOazxgFTWy_yK3LpxsE7EUC9Ryw?usp=sharing

