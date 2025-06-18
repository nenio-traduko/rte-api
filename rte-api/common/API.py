
from abc import ABC
from json import loads
from urllib.parse import urlparse, ParseResult
from requests import post, get, Response

class API(ABC):
    _base_url: ParseResult = urlparse("")
    _tokens: dict[str, str] = {}

    def auth(self, client_id: str, client_secret: str):
        token_url = self._base_url._replace(path="/token/oauth/").geturl()
        data = {'grant_type': 'client_credentials'}
        access_token_response = post(token_url, data=data, verify=True, allow_redirects=False, auth=(client_id, client_secret))
        self._tokens = loads(access_token_response.text)
    
    def get(self, path: str, params: dict[str, str]) -> Response:
        endpoint = self._base_url._replace(path=path).geturl()
        api_call_headers = {'Authorization': 'Bearer ' + self._tokens['access_token']}
        return get(endpoint, headers=api_call_headers, params=params, verify=True)
    
    def post(self, path: str, data: dict[str, str]) -> Response:
        endpoint = self._base_url._replace(path=path).geturl()
        api_call_headers = {'Authorization': 'Bearer ' + self._tokens['access_token']}
        return post(endpoint, headers=api_call_headers, json=data, verify=True)