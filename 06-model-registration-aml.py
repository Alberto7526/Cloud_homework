# 06-model-registration-azure.py
from azureml.core import Workspace
from azureml.core import Model

if __name__ == "__main__":
    ws = Workspace.from_config(path='./.azureml',_file_name='config.json')
    model = Model.register(model_name='nutrition_model',
                           tags={'area': 'tarea_udea','scoring' : 0.82576, 'data_set_size': 660},
                           model_path='outputs/nutrition_model.pkl',workspace = ws)
    print(model.name, model.id, model.version, sep='\t')