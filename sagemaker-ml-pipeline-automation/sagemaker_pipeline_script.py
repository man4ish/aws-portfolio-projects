import sagemaker
from sagemaker import get_execution_role
from sagemaker.pipeline import PipelineModel
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.workflow.steps import ProcessingStep, TrainingStep, ModelStep
from sagemaker.processing import ScriptProcessor
from sagemaker.sklearn.estimator import SKLearnEstimator
from sagemaker.inputs import TrainingInput
from sagemaker.model import Model
from sagemaker import get_execution_role

# Get the execution role
role = get_execution_role()

# Define the pipeline name
pipeline_name = "Titanic-Survival-Prediction-Pipeline"

# 1. Data Preprocessing Step (use a script for preprocessing)
preprocessing_script = 'preprocessing.py'  # A Python script for preprocessing the data
processing = ScriptProcessor(
    image_uri=sagemaker.image_uris.retrieve("sklearn", sagemaker.session.Session().boto_region_name),
    command=["python3"],
    instance_type="ml.m5.xlarge",
    instance_count=1,
    role=role,
)

processing_step = ProcessingStep(
    name="PreprocessData",
    processor=processing,
    inputs=[
        sagemaker.inputs.TrainingInput("s3://my-bucket/titanic-data.csv")
    ],
    outputs=[
        sagemaker.outputs.Output(output_name="processed_data", source="output_dir")
    ],
    code=preprocessing_script
)

# 2. Model Training Step (using a Scikit-learn estimator)
train_script = 'train_model.py'  # A Python script for training the model

sklearn_estimator = SKLearnEstimator(
    entry_point=train_script,
    role=role,
    instance_type="ml.m5.large",
    instance_count=1,
    framework_version="0.23-1",
    py_version="py3",
    script_mode=True,
)

training_step = TrainingStep(
    name="TrainModel",
    estimator=sklearn_estimator,
    inputs={
        "train": sagemaker.inputs.TrainingInput(
            s3_data=processing_step.properties.ProcessingOutputConfig.Outputs["processed_data"].S3Output.S3Uri,
            content_type="csv",
        )
    },
)

# 3. Model Evaluation Step
model_eval_script = 'evaluate_model.py'  # A Python script for model evaluation

model_evaluation = ScriptProcessor(
    image_uri=sagemaker.image_uris.retrieve("sklearn", sagemaker.session.Session().boto_region_name),
    command=["python3"],
    instance_type="ml.m5.xlarge",
    instance_count=1,
    role=role,
)

evaluation_step = ProcessingStep(
    name="EvaluateModel",
    processor=model_evaluation,
    inputs=[
        sagemaker.inputs.TrainingInput(
            s3_data=training_step.properties.ModelArtifacts.S3ModelArtifacts
        )
    ],
    outputs=[sagemaker.outputs.Output(output_name="evaluation_result", source="output_dir")],
    code=model_eval_script,
)

# 4. Model Registration Step
model = Model(
    image_uri=sagemaker.image_uris.retrieve("sklearn", sagemaker.session.Session().boto_region_name),
    role=role,
    model_data=training_step.properties.ModelArtifacts.S3ModelArtifacts,
)

model_step = ModelStep(
    name="RegisterModel",
    model=model,
    inputs={
        "Model": evaluation_step.properties.ProcessingOutputConfig.Outputs["evaluation_result"].S3Output.S3Uri
    },
)

# 5. Define the Pipeline
pipeline = Pipeline(
    name=pipeline_name,
    steps=[processing_step, training_step, evaluation_step, model_step],
)

# 6. Run the pipeline
pipeline.upsert(role_arn=role)
pipeline.start()

