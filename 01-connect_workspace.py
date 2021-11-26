from azureml.core.authentication import InteractiveLoginAuthentication
from azureml.core import Workspace

interactive_auth = InteractiveLoginAuthentication(force=True, tenant_id='99e1e721-7184-498e-8aff-b2ad4e53c1c2')

ws = Workspace.get(
    name='mlw-esp-udea-david-alberto',
    subscription_id='2ef15443-5c82-4c81-818a-2be2b061a27e',
    resource_group='rg-ml-udea-david-alberto',
    location='eastus2',
    auth=interactive_auth
)
ws.write_config(path='.azureml')


