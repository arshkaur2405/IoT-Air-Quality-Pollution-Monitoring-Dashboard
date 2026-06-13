from datetime import datetime
import os
import pandas as pd
from analytics.generate_analytics_report import (
    save_analytics_report
)

from analytics.analytics_engine import (
    calculate_statistics
)

from ml.pollution_predictor import (
    predict_next_aqi
)
os.makedirs(
    "data",
    exist_ok=True
)

os.makedirs(
    "outputs/reports",
    exist_ok=True
)

from simulation.sensor_simulator import generate_sensor_data
from simulation.aqi_calculator import (
    classify_aqi,
    health_recommendation
)

from simulation.alert_system import (
    generate_alert
)

from simulation.data_logger import (
    save_data
)

from simulation.report_generator import (
    generate_report
)

sensor_data = generate_sensor_data()

aqi = sensor_data["aqi"]

status = classify_aqi(aqi)

alert = generate_alert(aqi)

recommendation = health_recommendation(
    status
)

record = {

    "timestamp": datetime.now(),

    "aqi": aqi,

    "temperature":
    sensor_data["temperature"],

    "humidity":
    sensor_data["humidity"],

    "gas_level":
    sensor_data["gas_level"],

    "status":
    status,

    "alert":
    alert,

    "recommendation":
    recommendation
}

save_data(record)

generate_report(record)

print("\n")
print("=" * 50)
print("AIR QUALITY MONITOR")
print("=" * 50)

for key, value in record.items():

    print(
        f"{key}: {value}"
    )
try:

    df = pd.read_csv(
        "data/air_quality_log.csv"
    )

    stats = calculate_statistics(
        df
    )

    prediction = predict_next_aqi(
        "data/air_quality_log.csv"
    )

    print("\nANALYTICS")

    print(
        f"Average AQI: {stats['average_aqi']}"
    )

    print(
        f"Maximum AQI: {stats['max_aqi']}"
    )

    print(
        f"Minimum AQI: {stats['min_aqi']}"
    )

    print(
        f"Predicted Next AQI: {prediction}"
    )

except:

    pass
save_analytics_report(
    stats,
    prediction
)