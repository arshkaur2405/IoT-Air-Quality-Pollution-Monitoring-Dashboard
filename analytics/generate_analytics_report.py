# analytics/generate_analytics_report.py

import os


def save_analytics_report(
    stats,
    prediction
):

    os.makedirs(
        "outputs/reports",
        exist_ok=True
    )

    report = f"""
==================================
ANALYTICS REPORT
==================================

Total Records:
{stats['total_records']}

Average AQI:
{stats['average_aqi']}

Maximum AQI:
{stats['max_aqi']}

Minimum AQI:
{stats['min_aqi']}

Average Temperature:
{stats['average_temperature']}

Average Humidity:
{stats['average_humidity']}

Average Gas:
{stats['average_gas']}

Predicted Next AQI:
{prediction}
"""

    with open(
        "outputs/reports/analytics_report.txt",
        "w"
    ) as file:

        file.write(
            report
        )
        # ...