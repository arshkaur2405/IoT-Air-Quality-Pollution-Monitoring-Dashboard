# 🌍 Smart City Air Quality Intelligence Platform

## Industry-Oriented IoT Air Quality & Pollution Monitoring Dashboard

---

## 📌 Project Overview

The **Smart City Air Quality Intelligence Platform** is an industry-oriented IoT project that monitors environmental conditions such as air quality, temperature, humidity, and gas concentration. The system simulates real-world IoT sensors, performs Air Quality Index (AQI) analysis, generates alerts, stores environmental data, and visualizes pollution trends through an interactive dashboard.

This project is designed for students, IoT enthusiasts, and developers who want to understand environmental monitoring systems without requiring physical hardware.

---

## 🎯 Problem Statement

Air pollution is one of the major environmental challenges affecting public health and quality of life. Traditional monitoring systems are expensive and difficult to deploy at scale.

This project aims to create a cost-effective IoT-based monitoring solution capable of:

* Monitoring environmental conditions
* Classifying air quality levels
* Generating alerts for hazardous conditions
* Visualizing pollution trends
* Supporting smart city initiatives

---

## 🚀 Features

### Environmental Monitoring

* AQI Monitoring
* Temperature Monitoring
* Humidity Monitoring
* Gas Level Monitoring

### Air Quality Analysis

* AQI Classification
* Pollution Status Detection
* Health Recommendations
* Alert Generation

### Data Management

* Automatic Data Logging
* CSV Storage
* Report Generation
* Rolling Data Retention

### Analytics

* Average AQI Analysis
* Maximum AQI Detection
* Minimum AQI Detection
* Environmental Statistics

### Machine Learning

* AQI Prediction
* Trend Forecasting
* Historical Data Analysis

### Dashboard

* Real-Time Monitoring
* AQI Gauge
* KPI Cards
* Trend Visualization
* Pollution Distribution Analysis
* Health Advisory Section
* Downloadable Reports

---

## 🏗 System Architecture

```text
Virtual Sensors
(MQ135, MQ2, DHT11 Simulation)
            │
            ▼
     Sensor Simulator
            │
            ▼
     AQI Calculation
            │
            ▼
    Pollution Analysis
            │
            ▼
     Alert Generation
            │
            ▼
       Data Logger
            │
            ▼
        CSV Storage
            │
            ▼
      Analytics Engine
            │
            ▼
      ML Prediction
            │
            ▼
    Streamlit Dashboard
```

---

## 📂 Project Structure

```text
IoT-Air-Quality-Pollution-Monitoring-Dashboard/
│
├── main.py
├── generate_history.py
├── generate_live_data.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── simulation/
│   ├── sensor_simulator.py
│   ├── aqi_calculator.py
│   ├── alert_system.py
│   ├── data_logger.py
│   └── report_generator.py
│
├── analytics/
│   ├── analytics_engine.py
│   └── generate_analytics_report.py
│
├── ml/
│   └── pollution_predictor.py
│
├── dashboard/
│   └── streamlit_app.py
│
├── data/
│
├── outputs/
│   ├── reports/
│   └── charts/
│
├── docs/
└── images/
```

---

## ⚙️ Technologies Used

### Programming Language

* Python 3.x

### Libraries

* Streamlit
* Pandas
* NumPy
* Plotly
* Matplotlib
* Scikit-Learn

### Concepts

* IoT Simulation
* Data Analytics
* Machine Learning
* Environmental Monitoring
* Dashboard Development

---

## 🔧 Installation

### Clone Repository

```bash
git clone https://github.com/arshkaur2405/IoT-Air-Quality-Pollution-Monitoring-Dashboard.git
```

### Navigate to Project

```bash
cd IoT-Air-Quality-Pollution-Monitoring-Dashboard
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Step 1: Generate Historical Data

```bash
python generate_history.py
```

This creates initial environmental data for analytics and visualization.

### Step 2: Start Live Data Simulation

```bash
python generate_live_data.py
```

This continuously generates sensor readings.

### Step 3: Launch Dashboard

```bash
streamlit run dashboard/streamlit_app.py
```

---

## 📊 Dashboard Features

### KPI Cards

* AQI
* Temperature
* Humidity
* Gas Level
* Alert Status

### AQI Gauge

Displays current AQI level visually.

### Environmental Trends

* AQI Trend
* Temperature Trend
* Humidity Trend
* Gas Level Trend

### Analytics Summary

* Average AQI
* Maximum AQI
* Minimum AQI
* Total Records

### Pollution Distribution

Pie chart visualization of pollution categories.

### Health Advisory

Automatic recommendations based on AQI status.

---

## 📈 AQI Categories

| AQI Range | Category  |
| --------- | --------- |
| 0 - 100   | Good      |
| 101 - 200 | Moderate  |
| 201 - 300 | Poor      |
| 301 - 500 | Hazardous |

---

## 🤖 Machine Learning Module

The project includes a prediction engine that forecasts future AQI values using historical environmental data.

### Benefits

* Trend Analysis
* Future Pollution Estimation
* Predictive Monitoring

---

## 📄 Generated Outputs

### CSV Logs

```text
data/air_quality_log.csv
```

### Environmental Report

```text
outputs/reports/latest_report.txt
```

### Analytics Report

```text
outputs/reports/analytics_report.txt
```

---


## 💡 Future Improvements

* Real ESP32 Integration
* MQ135 Sensor Integration
* DHT11 Sensor Integration
* MQTT Communication
* Node-RED Dashboard
* Email Notifications
* SMS Alerts
* Cloud Deployment
* Mobile Application
* Multi-City Monitoring
* AI-Based Pollution Forecasting

---

## 🎓 Learning Outcomes

Through this project, I learned:

* IoT System Design
* Environmental Monitoring
* Sensor Data Simulation
* Data Logging
* Dashboard Development
* Data Analytics
* Machine Learning Basics
* Software Architecture
* Git & GitHub Workflow

---

## 💼 Resume Description

Developed a Smart City Air Quality Intelligence Platform using Python and Streamlit. The system simulates IoT environmental sensors, performs AQI classification, generates real-time alerts, stores environmental data, produces analytical reports, and visualizes pollution trends through an interactive dashboard. Implemented machine learning-based AQI prediction and scalable data retention mechanisms to emulate real-world environmental monitoring systems.

---

## 👨‍💻 Author

**Arshdeep Kaur**

B.Tech Student | IoT & Software Development Enthusiast

---

## ⭐ If you found this project useful, consider giving it a star.
