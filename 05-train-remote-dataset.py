# 05-run-pytorch-data.py
from azureml.core import Workspace
from azureml.core import Experiment
from azureml.core import Environment
from azureml.core import ScriptRunConfig
from azureml.core import Dataset

if __name__ == "__main__":
    ws = Workspace.from_config(path='./.azureml',_file_name='config.json')
    datastore = ws.get_default_datastore()
    dataset = Dataset.File.from_files(path=(datastore, 'datasets/nutrition'))

    experiment = Experiment(workspace=ws, name='train-nutrition-model-remote')

    config = ScriptRunConfig(
        source_directory='./src',
        script='train-remote.py',
        compute_target='homework-cluster',
        arguments=['--data_path', dataset.as_named_input('input').as_mount()]
    )
    # set up pytorch environment
    env = Environment.from_conda_specification(
        name='nutrition-aml-env',
        file_path='./.azureml/nutrition-aml-env.yml'
    )
    config.run_config.environment = env

    run = experiment.submit(config)

    aml_url = run.get_portal_url()
    print("Submitted to compute cluster. Click link below")
    print("")
    print(aml_url)
