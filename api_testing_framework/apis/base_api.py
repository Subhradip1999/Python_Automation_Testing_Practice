# Actual reusable apis, directly interacting using requests module

import requests
from api_testing_framework.utils.config import BASE_URL, HEADERS


class BaseAPI:

    def get(self, endpoint, param=None):
        return requests.get(BASE_URL + endpoint, headers=HEADERS, params=param)

    def post(self, endpoint, data):
        return requests.post(BASE_URL + endpoint, json=data, headers=HEADERS)

    def update(self, endpoint, data):
        return requests.put(BASE_URL + endpoint, json=data, headers=HEADERS)

    def delete(self, endpoint):
        return requests.delete(BASE_URL + endpoint, headers=HEADERS)
