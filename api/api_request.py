import requests

class APIRequest:
    @staticmethod
    def make_request(url):
        response = requests.get(url)
        return response
