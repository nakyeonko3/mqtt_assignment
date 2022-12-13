from flask import Flask, render_template, jsonify
from read_csv_file import get_senor_data_last_value
import mqtt

app=Flask(__name__)
bmp_sensor_value = 0

@app.route("/")
def frontPage():
    return render_template(template_name_or_list='index.html')

@app.route("/getBmpSensorData")
def getBmpSensorData():
    bmp_sensor_value = float(get_senor_data_last_value())
    return jsonify({"Sensor":bmp_sensor_value})

if __name__ == "__main__":
    mqtt.mqtt_init()
    app.run(host="0.0.0.0", port="5050", debug=True)