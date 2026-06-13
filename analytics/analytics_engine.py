import pandas as pd


def calculate_statistics(df):

    stats = {

        "total_records":
        len(df),

        "average_aqi":
        round(
            df["aqi"].mean(),
            2
        ),

        "max_aqi":
        int(
            df["aqi"].max()
        ),

        "min_aqi":
        int(
            df["aqi"].min()
        ),

        "average_temperature":
        round(
            df["temperature"].mean(),
            2
        ),

        "max_temperature":
        round(
            df["temperature"].max(),
            2
        ),

        "average_humidity":
        round(
            df["humidity"].mean(),
            2
        ),

        "average_gas":
        round(
            df["gas_level"].mean(),
            2
        )
    }

    return stats
# ...