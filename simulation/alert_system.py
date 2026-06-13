def generate_alert(aqi):

    if aqi <= 100:
        return "SAFE"

    elif aqi <= 200:
        return "WARNING"

    elif aqi <= 300:
        return "DANGER"

    else:
        return "EMERGENCY"


def alert_color(alert):

    colors = {

        "SAFE": "GREEN",

        "WARNING": "YELLOW",

        "DANGER": "ORANGE",

        "EMERGENCY": "RED"
    }

    return colors.get(
        alert,
        "UNKNOWN"
    )