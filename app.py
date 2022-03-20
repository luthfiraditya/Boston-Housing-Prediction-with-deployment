from flask import Flask, render_template,request,redirect
import pickle
import sklearn
import numpy as np



app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method=='POST':

        with open('lr_pickle','rb') as r:
            model=pickle.load(r)

        a=float(request.form['RM'])
        b=float(request.form['LSTAT'])
        c =float(request.form['INDUS'])
        d =float(request.form['PTRATIO'])
        e=float(request.form['TAX'])

        datas=np.array((a, b, c, d, e))
        datas=np.reshape(datas,(1,-1))

        price_prediction=model.predict(datas)[0]
        price_prediction=round(price_prediction)
        price_prediction=price_prediction*10000


        return render_template('hasil.html',prediction_text='Price Prediction is ${}'.format(price_prediction))

    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)