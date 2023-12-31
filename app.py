import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
scaler  = pickle.load(open("scaler.pkl",'rb')) #load the scaler


app = Flask(__name__) #starting point of application
model = pickle.load(open("regmodel.pkl",'rb')) #load the model

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    data =[float(x) for x in request.form.values()]
    final_input = scaler.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output = model.predict(final_input)[0]
    return render_template("home.html",prediction_text="The predicted price is {}".format(output))

@app.route('/predict_api',methods=['POST'])

def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output = model.predict(new_data)
    print(output[0])
    return jsonify(output[0])

if __name__ == '__main__':
    app.run(debug=True)
