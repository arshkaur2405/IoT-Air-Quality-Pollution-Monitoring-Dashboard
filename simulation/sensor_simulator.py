import random


def generate_sensor_data():

    aqi = random.randint(30, 450)

    temperature = round(
        random.uniform(18, 42),
        2
    )

    humidity = round(
        random.uniform(25, 90),
        2
    )

    gas_level = random.randint(
        50,
        500
    )

    return {
        "aqi": aqi,
        "temperature": temperature,
        "humidity": humidity,
        "gas_level": gas_level
    }