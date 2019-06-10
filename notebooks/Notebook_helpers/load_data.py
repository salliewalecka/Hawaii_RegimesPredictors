# File to read in the data in consistent splits and format
import pandas as pd
from sklearn.model_selection import train_test_split


#Comment out data prep if running VIF
def data_prep(df):
    df = df.astype({"id_spatial": "category", "Island": "category", "Habitat_Modification": "category", 
               "Invasive_Algae": "category", "Regime": "category", "Regime1": "category", 
               "Regime2": "category", "Regime3": "category", "Regime5": "category"})
    return df


def load_coral_data(complete=True, CV=True, convert_to_categorical=True):
    if complete:
        df = pd.read_csv("../Data/Hawaii_RegimesPredictors_complete.txt", sep="\t", decimal=",")
        train = pd.read_csv("../Data/Modeling/Predictors_complete_train.txt", sep='\t', decimal=",")
        val = pd.read_csv("../Data/Modeling/Predictors_complete_val.txt", sep='\t', decimal=",")
        test = pd.read_csv("../Data/Modeling/Predictors_complete_test.txt", sep='\t', decimal=",")
    else:
        df = pd.read_csv("../Data/Hawaii_RegimesPredictors.txt", sep="\t", decimal=",")
        train = pd.read_csv("../Data/Modeling/Predictors_raw_train.txt", sep='\t', decimal=",")
        val = pd.read_csv("../Data/Modeling/Predictors_raw_val.txt", sep='\t', decimal=",")
        test = pd.read_csv("../Data/Modeling/Predictors_raw_test.txt", sep='\t', decimal=",")
    
    if convert_to_categorical:
        df = data_prep(df)
        train = data_prep(train)
        val = data_prep(val)
        test = data_prep(test)
        
    if CV:
        train = train.append(val)
        train, _ = train_test_split(train, test_size=0.0, random_state = 47, shuffle=True)
        return df, train, test
    
    return df, train, val, test