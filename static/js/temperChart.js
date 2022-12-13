(async () => {
  const data = {
    labels: [],
    datasets: [
      {
        label: 'c',
        data: [],
        // borderColor: 'rgb(54,162,235)',
        borderColor: 'rgb(112, 108, 108)',
        backgroundColor: 'rgb(145,203,245)',
        borderWidth: 1,
      },
    ],
  };
  const config = {
    type: 'line',
    data,
    options: {
      plugins: {
        streaming: {
          duration: 10000,
          ttl: 60000,
          refresh: 1000,
        },
      },
      animation: false,
      interaction: {
        intersect: false,
      },
      scales: {
        x: {
          type: 'realtime',
          realtime: {
            onRefresh: (chart) => {
              chart.data.datasets.forEach(async (dataset) => {
                dataset.data.push({
                  x: Date.now(),
                  y: await getBmpSensorData(),
                });
              });
            },
          },
        },
        y: { beginAtZero: true },
      },
    },
  };

  const myChart = new Chart(document.getElementById('temperChart'), config);
})();
