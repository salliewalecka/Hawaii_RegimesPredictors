# File to read in the data in consistent splits and format


#Comment out data prep if running VIF
def data_prep(df):
    df = df.astype({"id_spatial": "category", "Island": "category", "Habitat_Modification": "category", 
               "Invasive_Algae": "category", "Regime": "category", "Regime1": "category", 
               "Regime2": "category", "Regime3": "category", "Regime5": "category"})
    return df


def load_coral_data(location, complete=True, convert_to_category=True):
    df = pd.read_csv("../Data/Hawaii_RegimesPredictors_complete.txt", sep="\t", decimal=",")
    train = pd.read_csv("../Data/Modeling/Predictors_complete_train.txt", sep='\t', decimal=",")
    test = pd.read_csv("../Data/Modeling/Predictors_complete_test.txt", sep='\t', decimal=",")
    
    df = data_prep(df)
    train = data_prep(train)
    test = data_prep(test)
    
    return df, train, test