# -*- coding: utf-8 -*-
"""
@author: david.alvarado@met.com
"""

from requests import post, get, Response
from datetime import datetime
from typing import Optional
import json

from abc import ABC

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
    
    def post(self, path: str, data: dict[str, str]) -> Response:
        endpoint = self._base_url._replace(path=path).geturl()
        api_call_headers = {'Authorization': 'Bearer ' + self._tokens['access_token']}
        return post(endpoint, headers=api_call_headers, json=data, verify=True)
    
    
    
class RTEAPI(API):
    def __init__(self, client_id: str, client_secret: str):
        self._base_url = urlparse("https://digital.iservices.rte-france.com/")
        self.auth(client_id=client_id, client_secret=client_secret)

class BigAdjustedAPI(RTEAPI):
    def __init__(self, client_id: str, client_secret: str):
        super().__init__(client_id, client_secret)
        self._api_path = "private_api/adjusted_consumption/v2/"

    def get_updated_data(self, update_date: datetime, update_time_slot: Optional[int] = None, range: str = "0-9999", service_point_type: Optional[str] = None):
        params = {
            "update_date": update_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "range": range
        }

        if update_time_slot is not None:
            params["update_time_slot"] = str(update_time_slot)

        if service_point_type is not None:
            params["service_point_type"] = service_point_type
        
        response = self.get(self._api_path + "updated_data", params)
        return response.json()

client_id = 'd894f158-40cd-4b6c-b98b-a17510a32714'
client_secret = 'bda11958-9561-4999-87d0-54e273a07143'

big_adjusted_api = BigAdjustedAPI(client_id, client_secret)