SmartRIVER forecast system
notebook created by GECOsistema Srl - Piazza Maltesta 21 Rimini (Italy) mail : home@gecosistema.it

DISCLAIMER: This notebook and related sample data are provided "as they are" only for demonstrational purposes, without warranty of any kind, either express or implied. The user is the sole responsible for any use of this notebook and GECOsistema will not be liable for any damages that the user may suffer in connection with using, modifying or distributing any part of this notebook.

The notebook is provided under Creative Commons CC BY-NC-SA license (https://creativecommons.org/licenses/by-nc-sa/4.0/ )


This self explaining commented notebook (paired with an example  .csv dataset) has been shared as Jupyter notebook (for Google Colab). 
The user is guided, step by step, to perform forecast from a time serie of discharge (TARGET variable)  and a few input features (Vx)

Main steps encoded in the notebook are.

DATA READ AND PREPARATION – loading the dataset with target and input features, performing basic operations such as filling missing values, normalizing the variables, dealing with the time information.
FEATURE DROP to remove uninformative features from database.
MODEL Tuning to test and tune many ML algorithms and identify the most performing one, also to identify informative features, ( in this example exploiting H2O AutoML libraries)
DEPLOY MODELS to save best performing models for  operational deploying
