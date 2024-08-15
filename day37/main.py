from datetime import datetime

import requests

USER_NAME = "seokhun"
TOKEN = "MY_TOKEN"
GRAPH_ID = "graph1"

pixela_edpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(url=pixela_edpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_edpoint}/{USER_NAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "ajisai",

}
header = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
print(response.text)

pixel_endpoint = f"{pixela_edpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": "1",
}
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=header)
print(response.text)

update_pixel_endpoint = f"{pixela_edpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{datetime.now().strftime('%Y%m%d')}"
update_pixel_config = {
    "quantity": "2",
}
response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=header)
print(response.text)

delete_pixel_endpoint = f"{pixela_edpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{datetime.now().strftime('%Y%m%d')}"
response = requests.delete(url=delete_pixel_endpoint, headers=header)
print(response.text)