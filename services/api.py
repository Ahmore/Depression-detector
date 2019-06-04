import requests
import json

AZURE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
API_URL = 'https://depression-detector-backend.herokuapp.com/api/'


def register(username, password):
    url = API_URL + 'registration'

    json_data = {
        'username': username,
        'password': password,
    }

    response = requests.post(url, json=json_data)
    return response.status_code == 200


def login(username, password):
    url = API_URL + 'authentication'

    json_data = {
        'username': username,
        'password': password,
    }

    response = requests.post(url, json=json_data)
    if response.status_code != 200:
        return None
    return response.json()["token"]


def logout(token):
    url = API_URL + 'authentication'

    headers = {'token': token}

    response = requests.delete(url, headers=headers)
    return response.status_code == 200


def get_azure_token(token):
    url = API_URL + 'azure'

    headers = {'token': token}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    return response.content.decode('utf8')


def get_azure_data(azure_token, image):
    face_api_url = AZURE_URL + 'detect'

    headers = {
        'Ocp-Apim-Subscription-Key': azure_token,
        'Content-Type': 'application/octet-stream'
    }

    params = {
        'returnFaceId': 'false',
        'returnFaceRectangle': 'false',
        'returnFaceAttributes': 'emotion',
    }

    response = requests.post(face_api_url, params=params, headers=headers, data=image)

    if len(response.json()) == 0:
        return None
    else:
        return response.json()[0].get('faceAttributes').get('emotion')


def send_measurement(token, date, value):
    url = API_URL + 'measurement'

    headers = {'token': token}

    json_data = {
        'date': date,
        'value': value,
    }

    response = requests.post(url, headers=headers, json=json_data)
    return response.status_code == 200


def get_measurements(token):
    url = API_URL + 'measurement'

    headers = {'token': token}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    return response.json()
