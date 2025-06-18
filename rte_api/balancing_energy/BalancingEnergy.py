from common import RTEAPI
from datetime import datetime
from typing import Optional

class BalancingEnergyAPI(RTEAPI):
    def __init__(self, client_id: str, client_secret: str):
        super().__init__(client_id, client_secret)
        self._api_path = "open_api/balancing_energy/v4/"

    def tso_offers(self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None):
        params: dict[str, str] = {}

        if start_date is not None and end_date is not None:
            params["start_date"] = start_date.strftime(self._date_time_format)
            params["end_date"] = end_date.strftime(self._date_time_format)
        else:
            raise ValueError("Both start_date and end_date must be provided.")

        response = self.get(self._api_path + "tso_offers", params)
        return response.json()