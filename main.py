import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "ojwbb620ijhb04w56",
    "username": "devansh18",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json= user_params)
#
# print(response.text)

graph = f"{pixela_endpoint}/devansh18/graphs"

graph_config = {
    "id": "cycle",
    "name": "cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": "ojwbb620ijhb04w56",
}

# response = requests.post(url=graph, json=graph_config, headers= headers)
# print(response.text)

pixel = f"{pixela_endpoint}/devansh18/garphs/cycle"

today = datetime.now()

pixel_date = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "18.2",
}

response = requests.post(url=pixel, json=pixel_date, headers=headers)

print(response.text)