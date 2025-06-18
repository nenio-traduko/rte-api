from common import RTEAPI
from datetime import datetime

class BalancingEnergyAPI(RTEAPI):
    def __init__(self, client_id: str, client_secret: str):
        super().__init__(client_id, client_secret)
        self._api_path = "open_api/balancing_energy/v4/"

    def tso_offers(self, start_date: datetime, end_date: datetime):
        params = {
            "start_date": start_date.strftime(self._date_time_format),
            "end_date": end_date.strftime(self._date_time_format)
        }

        response = self.get(self._api_path + "tso_offers", params)
        return response.json()