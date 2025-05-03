# Automating ML Workflow with SageMaker Pipelines

This repository demonstrates how to automate a machine learning workflow using **AWS SageMaker Pipelines**. It includes steps for:
- **Data Preprocessing**
- **Model Training**
- **Model Evaluation**
- **Model Registration**

## Services Used:
- **AWS SageMaker**
- **AWS S3**

## Prerequisites:
- AWS account with access to SageMaker
- AWS CLI configured (`aws configure`)
- Python 3.x
- SageMaker SDK installed: `pip install sagemaker`

## Setup:
1. Clone this repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Ensure that the Titanic dataset (`titanic.csv`) is available in your S3 bucket.

3. Create and upload the following scripts:
    - `preprocessing.py`: Handles data cleaning and preparation.
    - `train_model.py`: Trains the ML model using Scikit-learn.
    - `evaluate_model.py`: Evaluates the model's performance.

## Usage:
1. Execute the pipeline script:

    ```bash
    python sagemaker_pipeline_script.py
    ```

2. The pipeline will:
    - Preprocess data.
    - Train the model.
    - Evaluate the model.
    - Register the trained model in SageMaker Model Registry.

## Clean Up:
- Make sure to delete any unnecessary resources (SageMaker models, training jobs, etc.) to avoid incurring additional costs.
