import json
import numpy as np
import pandas as pd
import os
import joblib

def init():
    global model
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'nutrition_model.pkl')
    model = joblib.load(model_path)

def run(raw_data):
    columns= ['Hoja','Area','Perimetro','FF','Borde','Amarillo','Negro',
              'Rojo','Energia','contraste','disimilitud','correlacion','homogeneidad']

    data = np.array(json.loads(raw_data)['data'])
    pd_record = pd.DataFrame(data, index=None, columns=columns)

    del pd_record["Hoja"]
    #Divided by 10 because predicts 0,10,20,30...
    y_hat = int(model.predict(pd_record)/10)

    readmission = ['Sin deficiencia', 'Calcio','Boro', 'Fosforo', 'Nitrogeno', 
                   'Manganeso', 'Potasio', 'Zinc', 'Boro', 'Azufre', 'Hierro']

    return json.dumps({'Estado de deficiencia de la hoja: ' : readmission[int(y_hat)]})