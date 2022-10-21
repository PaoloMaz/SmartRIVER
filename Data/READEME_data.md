Example datasets: 

Discharge.csv   2 weeks dataset (default dataset for the notebook )

Dis = target variable ,  discharge in the next 14 days (m3/s) 
V1 = discharge in the antecedent 7 days (m3/s) 
V2 = precipitation in the antecedent 14 days [mm]
V3 = air temperature station 1 antecedent 3 days [°C]
V4 = relative humidity  station 1 in the antecedent 14 days [% 0-100]
V5 = ECMMWF precipitation forecast for the incoming 15 days the day before prediction day [kg m-2]

Discharge_m.csv   1 month  dataset
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

This asset has been developed in the 1st Open Call of I-NERGY 
(This project has received funding from the European Union's Horizon 2020 research and innovation programme within the framework 
of the I-NERGY Project, funded under grant agreement No 101016508)
