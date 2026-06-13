def classify_aqi(aqi):

    if aqi <= 100:
        return "GOOD"

    elif aqi <= 200:
        return "MODERATE"

    elif aqi <= 300:
        return "POOR"

    else:
        return "HAZARDOUS"


def health_recommendation(status):

    recommendations = {

        "GOOD":
        "Air quality is safe for outdoor activities.",

        "MODERATE":
        "Sensitive individuals should reduce prolonged outdoor exposure.",

        "POOR":
        "Limit outdoor activities and use masks if necessary.",

        "HAZARDOUS":
        "Stay indoors. Wear protective masks and avoid outdoor activities."
    }

    return recommendations.get(
        status,
        "No recommendation available."
    )
    # ..