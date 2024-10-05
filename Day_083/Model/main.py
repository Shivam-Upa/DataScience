import pickle
from flask import Flask, request, render_template
# from sklearn.preprocessing import StandardScaler as scaler

app = Flask(__name__)

model = pickle.load(open('C:/Users/upadh/flask/pro4/models/model.pkl', 'rb'))
scaler = pickle.load(open('C:/Users/upadh/flask/pro4/models/scaler.pkl', 'rb'))

@app.route('/', methods=['POST','GET'])
def data():
    if request.method=='POST':
        ES = float(request.form.get('ENGINE_SIZE'))
        CY = float(request.form.get('CYLINDERS'))
        FC = float(request.form.get('FUEL_CONSUMPTION'))

        data = scaler.transform([[ES, CY, FC]])

        result = model.predict(data)

        return render_template('index.html',results=result[0])
    
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)