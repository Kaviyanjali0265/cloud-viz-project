// Assuming your response contains a list of predictions, each with a 'prediction' and 'timestamp' field
var response = pm.response.json();


// Extract data for the chart
var labels = response.map(item => item.timestamp); // or any other field you want to use for labels
var data = response.map(item => item.prediction); // or any other field you want to plot


// HTML and JavaScript code for Chart.js
var template = `
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div style="width: 75%;">
        <canvas id="myChart"></canvas>
    </div>
    <script>
        var ctx = document.getElementById('myChart').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: {{labels}},
                datasets: [{
                    label: 'Predictions',
                    data: {{data}},
                    backgroundColor: 'rgba(128, 128, 128, 0.2)',
                    borderColor: 'rgba(0,0,0, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: 'Timestamp'
                        }
                    },
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Prediction'
                        }
                    }
                }
            }
        });
    </script>
</body>
</html>
`;


// Set up data to be injected into the template
var chartData = {
    labels: JSON.stringify(labels),
    data: JSON.stringify(data)
};


// Replace placeholders in the template with actual data
var htmlContent = template.replace('{{labels}}', chartData.labels).replace('{{data}}', chartData.data);


// Set the visualizer
pm.visualizer.set(htmlContent);
