import os


def generate_report(record):

    os.makedirs(
        "outputs/reports",
        exist_ok=True
    )

    report = f"""
==================================
AIR QUALITY REPORT
==================================

Timestamp : {record['timestamp']}

AQI : {record['aqi']}

Temperature : {record['temperature']} °C

Humidity : {record['humidity']} %

Gas Level : {record['gas_level']}

Status : {record['status']}

Alert : {record['alert']}

Recommendation :
{record['recommendation']}
"""

    with open(
        "outputs/reports/latest_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)
        # ..