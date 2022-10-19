SmartRIVER forecast system
notebook created by GECOsistema Srl - Piazza Maltesta 21 Rimini (Italy) mail : home@gecosistema.it

DISCLAIMER: This notebook and related sample data are provided "as they are" only for demonstrational purposes, without warranty of any kind, either express or implied. The user is the sole responsible for any use of this notebook and GECOsistema will not be liable for any damages that the user may suffer in connection with using, modifying or distributing any part of this notebook.

The notebook is provided under Creative Commons CC BY-NC-SA license (https://creativecommons.org/licenses/by-nc-sa/4.0/ )


This self-explaining commented notebook (paired with an example .csv dataset) has been shared as Jupyter notebook (tested in Google Colab and linked to Gdrive folder but can be easily adapted to run in other platforms). 
The notebook is structured in steps and guides the user in setting up a forecast system to predict next value in a time series of discharge (TARGET variable) using a few input features (Vx. Please refer to the example Discharge.csv dataset.
Main steps encoded in the notebook are: 
o	DATA READ AND PREPARATION – loading the dataset with target and input features, performing basic operations such as filling missing values, normalizing the variables, dealing with the time information.
o	FEATURE DROP to remove uninformative features from database, this can be done iteratively after running the ML models to identify most informative features
o	MODEL Tuning to test and tune many ML algorithms and identify the most performing one, also to identify informative features, ( n this example exploiting H2O AutoML libraries), please refer to H2O documentation (https://docs.h2o.ai/h2o/latest-stable/h2o-docs/automl.html) if you want to fine tune the parameters and use different models
o	DEPLOY MODELS to save best performing models for operational deploying
o	LOAD MODELS to load a saved model and run it over a test dataset
