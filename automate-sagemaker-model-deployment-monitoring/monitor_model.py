"""
monitor_model.py
----------------

This script monitors the SageMaker endpoint performance over time.
It checks for model drift and records any significant changes in accuracy.
"""

import boto3
import time
import matplotlib.pyplot as plt

# Initialize the SageMaker runtime
runtime_client = boto3.client('runtime.sagemaker')

# Endpoint name
endpoint_name = "sklearn-model-123456"  # Replace with actual endpoint

# Track performance over time
accuracy_values = []

# Simulate accuracy monitoring (in reality, you'd compare predicted vs actual values over time)
for i in range(10):  # Simulating 10 rounds of predictions
    sample_input = [[5.1, 3.5, 1.4, 0.2]]
    response = runtime_client.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType='application/json',
        Body=json.dumps(sample_input)
    )
    result = json.loads(response['Body'].read().decode())
    accuracy_values.append(result[0])  # Simulate accuracy as prediction value

    time.sleep(10)  # Simulate time delay for next check

# Plot the accuracy over time
plt.plot(accuracy_values)
plt.title('Model Accuracy over Time')
plt.xlabel('Time (in arbitrary units)')
plt.ylabel('Accuracy')
plt.savefig('model_accuracy_plot.png')
plt.show()
