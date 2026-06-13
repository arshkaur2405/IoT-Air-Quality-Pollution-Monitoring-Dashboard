import subprocess

TOTAL_RECORDS = 500

for i in range(
    TOTAL_RECORDS
):

    subprocess.run(
        ["python", "main.py"]
    )

    print(
        f"Generated {i+1}/{TOTAL_RECORDS}"
    )

print("\nHistory Generated Successfully")