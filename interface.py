from flask import Flask,render_template,request,url_for,jsonify

import config1
import pandas as pd
import numpy as np
import sklearn

from utils import Diabetes


app =Flask(__name__)

@app.route('/')
def man():
    return render_template('home.html')



@app.route('/predict',methods=['GET','POST'])

def outcome():

    if request.method == 'POST':


        data= request.form

        print ('data:' ,data)
        dia_data =Diabetes(data)

        dib_found =dia_data.get_predicted_outcome()

        return  render_template('after.html',data=dib_found)


if __name__ =='__main__':

    app.run('0.0.0.0',port=9090)