# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:05:52 2025

@author: david.alvarado@met.com
"""

from requests import post, get, Response
import json

from abc import ABC, abstractmethod

from urllib.parse import urlparse, ParseResult

class API(ABC):
    _base_url: ParseResult = urlparse("")
    _tokens: dict[str, str] = {}

    def auth(self, client_id: str, client_secret: str):
        token_url = self._base_url._replace(path="/token/oauth/").geturl()
        data = {'grant_type': 'client_credentials'}
        access_token_response = post(token_url, data=data, verify=True, allow_redirects=False, auth=(client_id, client_secret))
        self._tokens = json.loads(access_token_response.text)
    
    def get(self, path: str, params: dict[str, str]) -> Response:
        endpoint = self._base_url._replace(path=path).geturl()
        api_call_headers = {'Authorization': 'Bearer ' + self._tokens['access_token']}
        return get(endpoint, headers=api_call_headers, params=params, verify=True)
    
class RTEAPI(API):
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.tokens = self.auth()
        self.api_url = "https://digital.iservices.rte-france.com/private_api/"

    def auth(self):
        token_url = "https://digital.iservices.rte-france.com/token/oauth/"
        data = {'grant_type': 'client_credentials'}
        access_token_response = requests.post(token_url, data=data, verify=True, allow_redirects=False, auth=(self.client_id, self.client_secret))
        tokens = json.loads(access_token_response.text)
        return tokens

class RTEBigAdjustedAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.tokens = self.auth()
        self.api_url = "https://digital.iservices.rte-france.com/private_api/adjusted_consumption/v2/"

    def auth(self):
        token_url = "https://digital.iservices.rte-france.com/token/oauth/"
        data = {'grant_type': 'client_credentials'}
        access_token_response = requests.post(token_url, data=data, verify=True, allow_redirects=False, auth=(self.client_id, self.client_secret))
        tokens = json.loads(access_token_response.text)
        return tokens

client_id = 'd894f158-40cd-4b6c-b98b-a17510a32714'
client_secret = 'bda11958-9561-4999-87d0-54e273a07143'

big_adjusted_api = RTEBigAdjustedAPI(client_id, client_secret)