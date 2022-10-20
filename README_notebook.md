This self-explaining commented notebook (paired with an example .csv datasets) has been shared as Jupyter notebook (tested in Google Colab and linked to Gdrive folder but can be easily adapted to run in other platforms).

The notebook is structured in steps and guides the user in setting up a forecast system to predict next value in a time series of discharge (TARGET variable) using a few input features (Please refer to the example datasets explained hereafter)

Main steps encoded in the notebook are:

- DATA READ AND PREPARATION – loading the dataset with target and input features, performing basic operations such as filling missing values, normalizing the variables, dealing with the time information.
- FEATURE DROP to remove uninformative features from database, this can be done iteratively after running the ML models to identify most informative features
- MODEL Tuning to test and tune many ML algorithms and identify the most performing one, also to identify informative features, ( n this example exploiting H2O AutoML libraries), please refer to H2O documentation (https://docs.h2o.ai/h2o/latest-stable/h2o-docs/automl.html) if you want to fine tune the parameters and use different models
- DEPLOY MODELS to save best performing models for operational deploying
- LOAD MODELS to load a saved model and run it over a test dataset


Example datasets: 
Discharge.csv 2 weeks dataset (default dataset for the notebook ) 
Dis = target variable ,  discharge in the next 14 days (m3/s) 
V1 = discharge in the antecedent 7 days (m3/s) 
V2 = precipitation in the antecedent 14 days [mm]
V3 = air temperature station 1 antecedent 3 days [°C]
V4 = relative humidity  station 1 in the antecedent 14 days [% 0-100]
V5 = ECMMWF precipitation forecast for the incoming 15 days the day before prediction day [kg m-2]

Discharge_m.csv 1 month  dataset
Dis = target variable ,  discharge in the next 14 days (m3/s) 
V1 = discharge in the antecedent 1 month (m3/s)
V11= discharge in the incoming  month - climatic average of the past 5 years (m3/s)
V2 = precipitation in the antecedent 1 month  [mm]
V3 = air temperature station 1 antecedent 1 month [°C]
V4 = relative humidity  station 1 in the antecedent 1 month [% 0-100]
V5 = ECMMWF precipitation forecast for the incoming 15 days the day before prediction day [kg m-2]

daily_master dataset.csv
daily dataset of the target and input variables as retrieved 
Qin = observed incoming dicharge  (m3/s) 
P1 = precipitation statin 1   [mm]
T1 = air temperature station 1 [°C]
T2 = air temperature station 2 [°C]
RH1 = relative humidity  station 1  [% 0-100]
P15 = ECMMWF precipitation forecast for the incoming 15 days [kg m-2]

This asset has been developed in the 1st Open Call of I-NERGY (This project has received funding from the European Union's Horizon 2020 research and innovation programme within the framework of the I-NERGY Project, funded under grant agreement No 101016508)
