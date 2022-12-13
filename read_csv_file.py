import pandas as pd

save_data = {
    "save":0,
}

def get_senor_data_last_value(file_name ='sensor.csv'):
    try:
        df = pd.read_csv(file_name)
        last_number = df['Sensor'].values[-1]
        save_data["save"] = last_number
        return last_number
    except:
        return save_data["save"]