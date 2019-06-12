This repo was forked from JBjouffray/Hawaii_RegimesPredictors so it was traceable where we got our ideas/data from.  The original README is located at README-ORIGINAL.md.  The work done for CS229 at Stanford is in the /notebooks directory.

# Project

This project was created as part of a class project for [CSS229](http://cs229.stanford.edu/) taught at Stanford University. Our study focuses on analyzing how prediction accuracy of the coral regimes changes depending on the type of classification model used and its complexity. We take both continuous and factor inputs measuring human activity (e.g. new development) and environmental influences (e.g. wave power) and use them to predict the corresponding coral reef regime using a variety of classification methods.

# What's New

All the work for our CS229 project is the the /notebooks directory.  We left the other files from the previous paper in place. We create additional dataset features and also impute some missing data from the old data.

# What's Where

| File  | Content |
| ------------- | ------------- |
| notebooks/Train_Val_Test_Split.ipynb | Notebook for prepating Data |
| notebooks/EDA.ipynb | Exploratory Data Analysis for dataset |
| notebooks/NA_estimation.ipynb | Imputation of missing data for complexity and depth|
| notebooks/Feature Engineering.ipynb | Additional features engineered |
| notebooks/Baseline_Logistic_Model.ipynb | Initial Logistic Regression Model |
| notebooks/Logistic_Regressions_with_Error_Analysis.ipynb | Iterations on Logistic with in depth error analysis|
| notebooks/Feature-Engineered-Logistic.ipynb	| Logisic with additional features added |
| notebooks/SVMs.ipynb | Initial SVMs |
| notebooks/Feature-Engineered-SVMs.ipynb | SVM with additional features |
| notebooks/Random_Forest.ipynb | Most sucessful model which was also run with test set |
| notebooks/Gradient_Boosted_Trees.ipynb | Another variant of tree explored |
| notebooks/PCA.ipynb | Exploratory work on data to try and understand why we might not be classifying some classescorrectly |
| notebooks/Neural-Net.ipynb| Legacy NN code that was not included in write-up |



# Overall Results

![results-image](/results.jpeg)
