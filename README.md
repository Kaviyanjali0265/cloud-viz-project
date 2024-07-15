
# cloud-viz-project - AWS ML Pipeline and Visualization Suite

## Project Overview

CloudViz is a comprehensive Machine learning pipeline built on AWS Cloud that automates data preprocessing, model training, model deployment and visualization. The project utilizes various AWS Services and delivers an end to end seamless Elastic search service solutions.

## Architecture

![Architecture Diagram](Architecture Diagram)

## Features 

- **Data Storage**: Amazon S3 is used for storing raw and processed data after the Data Preprocessing step.
- **Data Preprocessing**: Data is preprocessed for cleaning and transforming data.
- **Model Training & Deployment**: AWS Sage maker service is used to train the ML model and deploy it in their respective endpoints.
- **Prediction Service**: AWS lambda functions are used to make predictions for the deployed model. Two functions are used for this purpose namely inference and retrieve.
- **API Management**: AWS API Gateway is used to create APIs for Prediction services.
- **Monitoring and Logging**: AWS CloudWatch monitors system performance and logs relevant metrics. Various services like Alarms, Log groups, Metrics are used as a means of troubleshooting mechanism.
- **Data Storage**: AWS DynamoDB is utilized to store the results of prediction in the form of a table which has two attributes namely "Timestamp and Prediction".
- **Indexing and Visualization**: Postman API is used for indexing and testing the deployed endpoint to execute this process. It helps in efficient and seamless search and quick retrieval of data from the index in which it is stored. Visualization is performed for the above results.

## Getting Started

### Prerequisites

  - AWS Account (Free Tier can be used)
  - Postman API
  - ML Model
  - Boto3
  - Python 3.x

## AWS Services used in CloudViz Project

- AWS SageMaker - Jupyter Notebook, Endpoints
- S3 - Bucket
- Lambda - Function
- API Gateway - Stages, Resources
- CloudWatch - Alarms, Metrics, Loggroups
- DynamoDB - Table
- Postman - Querying, Visualization
- IAM - Policies, Role

### Steps

1. **Clone the repository**:
   ```
   sh
   git clone https://github.com/Kamala0910/cloud-viz-project.git
   ```
2. **Configure AWS Resources**:
   - Setup S3 Buckets
   - Configure Sagemaker
   - Setup Lambda functions
   - Configure API Gateway
   - Setup Cloudwatch alarms and logging
   - Create DynamoDB Tables

## Usage

1. Upload the required dataset in the configured S3 bucket.
2. Create a new JUPYTER NOTEBOOK instance in SageMaker and perform the data preprocessing task by referring the link of the bucket created where the dataset is stored.
3. Build the ML Model and train the model.
    In this project, iris dataset is used. It consists of physical parameters of three species of flower — Versicolor, Setosa and Virginica. The numeric parameters which the dataset contains are Sepal width, Sepal length, Petal width and Petal length. In this data we will be predicting the classes of the flowers based on these parameters which will be the problem statement. For the purpose of creating the classifcation model XGBoost is used.
4. Train the model.
5. Deploy the model.
6. Invoke the specific lambda functions via API Gateway to get predictions and post the results. Create methods POST and GET under Resources for the respective Stage in the API Gateway Dashboard. Use the endpoint just generated to properly configure and setup the connection of Endpoints in POSTMAN API to perform querying.
7. Create CloudWatch Alarms, Loggroups, Metrics as a monitoring and troubleshoot mechanism to figure out and mitigate 5xx Server Errors in the Cloudwatch console. As one of the steps in creating Alarms, creating an SNS Topic and subscribing to it is required to receive any notification that AWS wants to send to the given active email id of the user incase the Alarm gets triggered.

## Required IAM POLICIES

- CloudWatchLogsFullAccess
- AmazonDynamoDBFullAccess
- AmazonSageMakerFullAccess
- AWSLambdaBasicExecutionRole

## APIS

### Endpoints

**POST METHOD** - to find predictions
  **Request**
  ```json
{"input_data":[data]}
  ```
Eg: 
{"x1":6.7,"x2":3.3,"x3":5.7,"x4":2.5}
**GET METHOD** - to retrieve results
  **Response**
  ```json
{"prediction":result}
  ```
Eg:
{"prediction": 1,
"timestamp":""}

## License 

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## Authors

Kaviyanjali(https://github.com/Kaviyanjali0265)
Kamala(https://github.com/Kamala0910)


## References
- [AWS SageMaker](https://docs.aws.amazon.com/sagemaker/)
- [AWS Lambda](https://docs.aws.amazon.com/lambda/)
- [AWS IAM](https://docs.aws.amazon.com/iam/)
- [AWS CloudWatch](https://docs.aws.amazon.com/cloudwatch/)
- [AWS S3](https://docs.aws.amazon.com/s3/)
- [AWS API Gateway](https://docs.aws.amazon.com/apigateway/)
- [AWS DynamoDB](https://docs.aws.amazon.com/dynamodb/)
- [Postman API](https://learning.postman.com/docs/introduction/overview/)
