import pandas as pd
from datetime import datetime

df = pd.DataFrame([], columns=['Date', 'Sensor'])

def make_csvfile(sensor_value):
    global df
    new_line = pd.DataFrame({
            'Date': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
            'Sensor': [sensor_value]
            })
    df = pd.concat([df, new_line], ignore_index=True)
    df.to_csv('sensor.csv', index=False)