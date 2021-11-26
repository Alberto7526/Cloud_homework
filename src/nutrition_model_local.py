import pickle
import pandas as pd
import numpy as np
import json

#load the model

with open('../outputs/nutrition_model.pkl', 'rb') as model_pkl:
    rf = pickle.load(model_pkl)

if __name__ == "__main__":
    columns= ['Hoja','Area','Perimetro','FF','Borde','Amarillo','Negro',
              'Rojo','Energia','contraste','disimilitud','correlacion','homogeneidad']

    data = np.array([[2476486.5,7066.212995,1.604451538,0,0,0,0,0.3422,51.9402,1.2775,0.9639,0.7046,0]])
    pd_record = pd.DataFrame(data, index=None, columns=columns)
    del pd_record["Hoja"]
    #Divided by 10 because predicts 0,10,20,30...
    prediction = int(rf.predict(pd_record)/10)
    state = ['Sin deficiencia', 'Calcio','Boro', 'Fosforo', 'Nitrogeno', 
                   'Manganeso', 'Potasio', 'Zinc', 'Boro', 'Azufre', 'Hierro']
    result = print({'Estado de deficiencia de la hoja: ' : state[int(prediction)]})
    print(result)