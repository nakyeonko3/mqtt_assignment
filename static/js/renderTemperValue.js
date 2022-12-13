let count = 23;
const temperValueElement = document.getElementById('temperValue');

const getBmpSensorData = () => {
  return fetch('/getBmpSensorData')
    .then((response) => response.json())
    .then((data) => data.Sensor);
};

const renderTemperValue = async () => {
  temperValueElement.innerText = await getBmpSensorData();
};

const init = () => {
  setInterval(renderTemperValue, 1000);
};

init();
