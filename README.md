# Energy Consumption and Weather Prediction System

## Overview

This project aims to develop a robust prediction or forecasting system using data mining techniques. It encompasses four key components: data collection and preprocessing, exploratory data analysis, model selection and training, and model evaluation. The dataset used is sourced from Kaggle, focusing on hourly energy demand generation and weather information.

## Components

### Data Collection

The dataset includes information on energy consumption, generation prices, and weather. Data was sourced from Kaggle and subsequently cleaned and preprocessed.

### Data Cleaning

- **Checking/Removing Null Values**: Null values were identified and addressed.
- **Checking/Removing Duplicates**: Duplicate rows were identified and removed.
- **Dropping Irrelevant Columns**: Columns deemed unnecessary for analysis were dropped.
- **Checking/Removing Outliers and Noise**: Outlier analysis was performed, and outliers were removed from the dataset.

### Data Pre-processing

- **Feature Creation**: Additional temporal features were extracted and derived from the dataset.
- **Checking for Skewness and Attribute Transformation**: Skewness correction and transformation were performed on the dataset.
- **Encoding Columns**: Categorical variables were transformed into numerical representations using label encoding.

### Exploratory Data Analysis (EDA)

- **Identifying Patterns, Trends, and Correlations**: Correlation between columns was computed and visualized.
- **Visualizing Data Using Appropriate Plots**: Data distribution was visualized using appropriate plots.
- **Feature Subset Selection**: Feature subset selection was performed using a random forest regression model.

### Model Selection and Training

- **Test-Train Split**: The dataset was split into training and testing sets.
- **Checking for Data Stationarity**: The stationarity of the data was verified.
- **Applying Different Models**: Various models including Linear Regression, Random Forest Regressor, XGBoost, and Decision Tree were trained and evaluated.

### Model Evaluation

- Models were evaluated based on accuracy, Mean Absolute Error, Mean Squared Error, and Root Mean Squared Error.

### Model Optimization

- Models were optimized for better performance.

### Front-end Interface

- Pickle files were created to store the optimized regression models.
- Integration of models' prediction with a front-end interface was achieved, where users can input the 5 best features and the model predicts the actual temperature.

## Results

The integration of models' prediction with the front-end interface allows users to predict the actual temperature based on selected features. 

## Conclusion

This project demonstrates the development of a comprehensive energy consumption and weather prediction system, integrating data mining techniques, exploratory data analysis, model selection, and evaluation. The system provides valuable insights for forecasting temperature and can be further enhanced for real-world applications.
