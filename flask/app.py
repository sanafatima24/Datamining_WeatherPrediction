from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import power_transform


app = Flask(__name__)

# Load the pickle file
with open('weather_pred_dt.pkl', 'rb') as file:
    model = pickle.load(file)
with open('weather_pred_lr.pkl', 'rb') as file:
    model2 = pickle.load(file)  
# with open('weather_pred_rf.pkl', 'rb') as file:
#     model3 = pickle.load(file)  
# with open('weather_pred_xgb.pkl', 'rb') as file:
#     model4 = pickle.load(file)    


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    wind_deg = float(request.form['wind_deg'])
    pressure = float(request.form['pressure'])
    humidity = float(request.form['humidity'])
    temp_max = float(request.form['temp_max'])
    temp_min = float(request.form['temp_min'])
    #make df of above values
    df=pd.DataFrame([wind_deg, pressure, humidity, temp_max, temp_min])
    df=df.T
    print(df)
 
    prediction = model.predict(df)
    prediction2 = model2.predict(df)
    # prediction3 = model3.predict(df)
    # prediction4 = model4.predict(df)

    #max repeated value
    prediction=max(prediction, prediction2)
    
    #fix to 2 decimal places
    prediction=np.round(prediction, 2)
    
    # Render the result template with the prediction
    return render_template('result.html', prediction=prediction)
if __name__ == '__main__':
    app.run()
