# File to read in the data in consistent splits and format
import pandas as pd
import numpy as np
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

def get_features_and_response(df, with_feature_eng = False):
    FIRST_PRED_IDX = 16
    LAST_OG_PRED_IDX = 36
    FIRST_FE_PRED_IDX = 41
    LAST_FE_PRED_IDX = 46
    if with_feature_eng:
        features =  df.iloc[:, np.r_[FIRST_PRED_IDX:LAST_OG_PRED_IDX, FIRST_FE_PRED_IDX:LAST_FE_PRED_IDX]]
        pred_names = features.columns
    else :
        features = df.iloc[:, FIRST_PRED_IDX:LAST_OG_PRED_IDX]
        pred_names = df.iloc[:,FIRST_PRED_IDX:LAST_OG_PRED_IDX].columns

    response = df['Regime']
    return features, response, pred_names