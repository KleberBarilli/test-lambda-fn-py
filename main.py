import msal
import requests

# configuração de autenticação
CLIENT_ID = '<seu_client_id>'
CLIENT_SECRET = '<seu_client_secret>'
REDIRECT_URI = 'http://localhost:8000'
AUTHORITY = 'https://login.microsoftonline.com/common'

# configuração do Microsoft Graph API
API_VERSION = 'v1.0'
DRIVE_ITEM_URL = f'https://graph.microsoft.com/{API_VERSION}/me/drive/root:/{filename}:/content'

# criar o objeto de autenticação do MSAL
app = msal.ConfidentialClientApplication(
    client_id=CLIENT_ID,
    client_credential=CLIENT_SECRET,
    authority=AUTHORITY
)

# autenticar o usuário
result = None
accounts = app.get_accounts()
if accounts:
    result = app.acquire_token_silent(
        scopes=['User.Read', 'Files.Read.All'],
        account=accounts[0]
    )

if not result:
    flow = app.initiate_device_flow(scopes=['User.Read', 'Files.Read.All'])
    print(flow['message'])
    result = app.acquire_token_by_device_flow(flow)

if 'access_token' in result:
    access_token = result['access_token']

    # enviar solicitação HTTP para obter o conteúdo do arquivo
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    response = requests.get(DRIVE_ITEM_URL, headers=headers)

    # salvar o conteúdo do arquivo em um arquivo local
    with open('file.xlsx', 'wb') as f:
        f.write(response.content)
else:
    print(result.get('error_description', 'Erro de autenticação'))
