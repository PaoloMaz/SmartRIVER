This self-explaining commented notebook (paired with an example .csv dataset) has been shared as Jupyter notebook (tested in Google Colab and linked to Gdrive folder but can be easily adapted to run in other platforms).

The notebook is structured in steps and guides the user in setting up a forecast system to predict next value in a time series of discharge (TARGET variable) using a few input features (Vx. Please refer to the example Discharge.csv dataset.

Main steps encoded in the notebook are:

- DATA READ AND PREPARATION – loading the dataset with target and input features, performing basic operations such as filling missing values, normalizing the variables, dealing with the time information.
- FEATURE DROP to remove uninformative features from database, this can be done iteratively after running the ML models to identify most informative features
- MODEL Tuning to test and tune many ML algorithms and identify the most performing one, also to identify informative features, ( n this example exploiting H2O AutoML libraries), please refer to H2O documentation (https://docs.h2o.ai/h2o/latest-stable/h2o-docs/automl.html) if you want to fine tune the parameters and use different models
- DEPLOY MODELS to save best performing models for operational deploying
- LOAD MODELS to load a saved model and run it over a test dataset

This asset has been developed in the 1st Open Call of I-NERGY (This project has received funding from the European Union's Horizon 2020 research and innovation programme within the framework of the I-NERGY Project, funded under grant agreement No 101016508)
