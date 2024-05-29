# AUTOML - GRSTB Signal Traffic Image Classification

In this project we 'll use the German Traffic Signalisation image to create an Azure Machine Learning AUTOML classification Job

More information at : https://benchmark.ini.rub.de/



## Data Preparation 

The data set has been downloaded on our azure machine learning default data store to the following path: `lab-data/gtsrb-german-traffic-sign/`



## Authentication 

The following env variable must be set in an `.env` file in the root of the project:


```
AZURE_SUBSCRIPTION_ID=<your subscription ID>
AZURE_RESOURCE_GROUP=<name of the resource group of Azure ML>
AZURE_WORKSPACE=azure=<name of the workspace>
AZURE_TENANT_ID=<your tenant ID>
AZURE_CLIENT_ID=<client ID of the service principal associated with your workspace>
AZURE_CLIENT_SECRET=<client secret of the service principal associated with your workspace>
```
