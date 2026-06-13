import os
import pandas as pd
from pandas.errors import EmptyDataError

CSV_FILE = "data/air_quality_log.csv"

# Keep only latest records
MAX_RECORDS = 500


def save_data(record):

    # Create data folder if missing
    os.makedirs(
        "data",
        exist_ok=True
    )

    new_df = pd.DataFrame([record])

    try:

        # Existing file available
        if os.path.exists(CSV_FILE):

            old_df = pd.read_csv(
                CSV_FILE
            )

            df = pd.concat(
                [old_df, new_df],
                ignore_index=True
            )

        else:

            df = new_df

    except (EmptyDataError, pd.errors.ParserError):

        # Recover from empty/corrupted file
        df = new_df

    # ----------------------------------
    # Rolling Window Storage
    # Keep only latest 500 records
    # ----------------------------------

    if len(df) > MAX_RECORDS:

        df = df.tail(
            MAX_RECORDS
        ).reset_index(
            drop=True
        )

    # Save updated data

    df.to_csv(
        CSV_FILE,
        index=False
    )

    return len(df)