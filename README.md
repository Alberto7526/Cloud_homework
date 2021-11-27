# Despliegue de modelo para detección de deficiencias nutricionales en hojas de café desde Azure

##### Integrantes: 
Victor Alberto Lizcano Portilla		alberto.lizcano@udea.edu.co

David Alberto Rodriguez Muñoz		dalberto.rodriguez@udea.edu.co
##### Trabajo final de Cloud - Cohorte 2-2021

## DESCRIPCIÓN DEL DATASET 

El conjunto de datos utilizado para este dataset es de un antigüo proyecto de tesis de uno de los compañeros del trabajo. Corresponde a datos extraídos de imágenes de hojas de café. El problema que dió origen al dataset es llamado “Detección de deficiencias nutricionales en plantas de café utilizando procesamiento digital de imágenes”. El dataset se encuentra conformado por los vectores patrón que describen las características de cada imagen (características de forma, color y textura).

## WORKFLOW EN AZURE

Siguiendo la ruta del workflow para Azure machine learning, se obtienen los siguientes pasos para la puesta en producción del modelo.

## CREACIÓN DEL WORKSPACE

Para la creación del workspace, inicialmente fue necesario crear el grupo de recursos, para este caso el “rg-ml-udea-david-alberto”, la nomenclatura de cada elemento se realizó siguiendo los lineamientos vistos en clase.   

Seguido a la creación del grupo de recursos se procede a configurar los diferentes ambientes de trabajo, instalando todos los paquetes necesarios para su correcto funcionamiento, esto se realiza utilizando los archivos yamel “nutrition-aml-env.yml” y “nutrition-local-env.yml”. Posteriormente nos conectamos al espacio de trabajo en azure, utilizando el siguiente script “01-connect_workspace.py”, el cual genera un archivo de configuración llamado config.json


Finalmente se realizó un test para confirmar la correcta conexión con el espacio de trabajo en azurE. 


## ENTRENAMIENTO DEL MODELO

Ya con el workspace creado, se prosiguió a crear el dataset en el workspace, por facilidad se utilizaron los scripts del repositorio original y se acoplaron las rutas de nuestro trabajo.  Después de ejecutar el script podemos verificar que el dataset se encuentra ya en nuestro workspace de Azure.

Una vez con los datos en el workspace se continúa con el entrenamiento del modelo de manera remota en la nube de azure. Utilizando el script “05-train-remote-dataset.py” para entrenamiento remoto, se crean 4 objetos esenciales en este paso; dataset objeto que se especifica en que path se encuentran los datos en nuestro workspace, experiment se crea el experimento en el workspace, config se crean las configuraciones del script de entrenamiento, y por último, env donde especificamos cual es el ambiente virtual que se utilizará para entrenar el modelo en nuestro workspace. Al finalizar las configuraciones este script se ejecuta y podemos ver los resultados del experimento en el Azure ML studio, el cual muestra un score de 0.826.

## REGISTRO Y DESPLIEGUE DEL MODELO

Luego de haber realizado el entrenamiento del modelo de manera remota y su correspondiente test, se procede a registrar el modelo, para ello se hizo uso del siguiente script “06-model-registration-azure.py”.


Para el despliegue del modelo, etapa en la cual se planea colocar el modelo en producción, se utilizaron los siguientes scripts para realizar el proceso de manera local “07-deploy-model-local.py” y de manera remota con ayuda de la nube de Azure, el script “08-deploy-model-remote.py”.  


# PRUEBA DEL MODELO

Para consumir el modelo creado como un servicio, se puede realizar una petición POST al siguiente link:

http://bb3f6b19-a776-48db-a1d8-2a097cadbf55.eastus2.azurecontainer.io/score

Y, utilizando el siguiente dato, se puede probar que predicción genera el modelo.

**{
    "data": 
        [
            [2476486.5,7066.212995,1.604451538,0,0,0,0,0.3422,51.9402,1.2775,0.9639,0.7046,0]
        ]
}**
