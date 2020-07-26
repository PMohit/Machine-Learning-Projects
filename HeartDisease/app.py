# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'new_regression_model_heart.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()
    
    if request.method == 'POST':
        
            
        Pregnancies = int(request.form['Pregnancies'])      
        Glucose = float(request.form['Glucose'])
        BloodPressure = float(request.form['BloodPressure'])
        SkinThickness = float(request.form['SkinThickness'])
        Insulin = float(request.form['Insulin']) 
        BMI = float(request.form['BMI'])          
        DiabetesPedigreeFunction = int(request.form['DiabetesPedigreeFunction'])      
        Age = int(request.form['Age'])          


        
        temp_array = [Pregnancies, Glucose, BloodPressure, SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]        
        
        data = np.array([temp_array])       
        my_prediction = int(model.predict(data)[0])

        if my_prediction<0:
            return render_template('result.html',prediction_texts="Hurray!! you don't have a heart disease.Stay Healty")
        else:
            return render_template('result.html',prediction_text="You have a heart disease pls consult your doctor ".format(my_prediction))
              


if __name__ == '__main__':
	app.run(debug=True)