"""
Modeling helper functions
"""
import pandas as pd
from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt

def evaluate_performance(test_y, test_pred, print_vals=True):
    cnf_matrix = metrics.confusion_matrix(test_y, test_pred)
    
    class_names=['Reg 1', 'Reg 2', 'Reg 3', 'Reg 5']
    cnf_matrix = pd.DataFrame(cnf_matrix, index = class_names,
                  columns = class_names)
    
    # plot confusion matrix with heatmap
    sns.heatmap(cnf_matrix, annot=True, cmap="YlGnBu" ,fmt='g')
    plt.tight_layout()
    plt.title('Confusion matrix', y=1.1)
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')
    
    if print_vals :
        count_misclassified = (test_y != test_pred).sum()
        print('Misclassified samples: {}'.format(count_misclassified))
        accuracy = metrics.accuracy_score(test_y, test_pred)    
        print('Classification Report:')
        print(metrics.classification_report(test_y, test_pred))  

def microaveage_F1(test_y, test_pred):
    return metrics.classification_report(test_y, test_pred, output_dict=True)['weighted avg']['f1-score']