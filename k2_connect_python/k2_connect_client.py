"""This is the k2 connect layer facilitating connection different K2 API services """
from .auth_layer import auth_layer


class K2_connect_client:
    def __init__(self, k2_api_token=None):
        self.k2_api_token = k2_api_token
