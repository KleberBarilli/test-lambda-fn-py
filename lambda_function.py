# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# def lambda_handler(event, context):

#     scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
#     credentials = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
#     client = gspread.authorize(credentials)
    

#     try:
#         sheet = client.open_by_key("1654386463").get_worksheet(0)
           
#         data = sheet.get_all_values()

#         print(data)

#     except Exception as e:
#         print("error",str(e))
 

# import requests
# import json

# # Autenticação com o Microsoft Graph

# headers = {
#     'Authorization': 'Bearer {token}',
#     'Content-Type': 'application/json'
# }


# url = "https://graph.microsoft.com/v1.0/drives/{drive-id}/items/{item-id}/workbook/worksheets/{sheet-name}/range(address='A1:Z100')"

# # Faz a requisição GET para ler os dados da planilha

# response = requests.get(url, headers=headers)


# if response.status_code == 200:
#     data = response.json()
#     values = data['values']
#     print(values)
# else:
#     print("Erro ao ler os dados da planilha:", response.text)
