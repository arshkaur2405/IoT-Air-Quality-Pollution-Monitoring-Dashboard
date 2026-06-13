import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


def predict_next_aqi(csv_file):

    try:

        df = pd.read_csv(
            csv_file
        )

        if len(df) < 5:

            return None

        X = np.arange(
            len(df)
        ).reshape(-1, 1)

        y = df["aqi"]

        model = LinearRegression()

        model.fit(
            X,
            y
        )

        future = np.array(
            [[len(df)]]
        )

        prediction = model.predict(
            future
        )[0]

        return round(
            prediction,
            2
        )

    except:

        return None