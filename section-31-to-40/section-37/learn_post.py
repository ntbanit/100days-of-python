import requests
import datetime
TOKEN = 'my_super_secret_token'
USER_NAME = 'anthecoder'
request_body = {
    'token': TOKEN,
    'username': USER_NAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
pixela_url ='https://pixe.la/v1/users'
requests.packages.urllib3.disable_warnings()
# response = requests.post(url=pixela_url, json=request_body, verify=False)
# print(response.text)

headers = {
    'X-USER-TOKEN': TOKEN
}
GRAPH_ID = 'my-yoga-graph'
payload = {
    'id': GRAPH_ID,
    'name': 'My Yoga Daily Routine',
    'unit': 'minutes',
    'type': 'int',
    'color': 'shibafu',
    'timezone': 'Asia/Ho_Chi_Minh'
}
register_graph_url = f'{pixela_url}/{USER_NAME}/graphs'
# response = requests.post(url=register_graph_url, json=payload, headers=headers, verify=False)
# print(response.text)

post_a_pixel_url = f'{pixela_url}/{USER_NAME}/graphs/{GRAPH_ID}'
today = datetime.date.today().strftime('%Y%m%d')

# completely useless in the website
optional_data ={
    'sleep': 5,
    'water': 1800,
    'burned_calories': 60,
    'Comment': 'Started my yoga routine on Pixela'
}
import json
yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y%m%d')
# payload = {
#     'date': yesterday,
#     'quantity': '20',
# }
print(yesterday)
payload = {
    'quantity': '15'
}
update_a_pixel_url =  f'{pixela_url}/{USER_NAME}/graphs/{GRAPH_ID}/{yesterday}'
delete_a_pixel_url =  f'{pixela_url}/{USER_NAME}/graphs/{GRAPH_ID}/{yesterday}'
request_loop = True
while request_loop :
    # response = requests.post(url=post_a_pixel_url, json=payload, headers=headers, verify=False)
    # response = requests.put(url=update_a_pixel_url, json=payload, headers=headers, verify=False)
    response = requests.delete(url=delete_a_pixel_url, headers=headers, verify=False)
    if "Please retry this request." not in response:
       request_loop = False
    else :
        print("Retry")
print(response.text)