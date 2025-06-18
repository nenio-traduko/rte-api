from common import RTEAPI
from datetime import datetime
from typing import Optional

class BalancingEnergyAPI(RTEAPI):
    def __init__(self, client_id: str, client_secret: str):
        super().__init__(client_id, client_secret)
        self._api_path = "open_api/balancing_energy/v4/"

    def tso_offers(self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None):
        try:
            params: dict[str, str] = self._optional_date_range_params(start_date, end_date)
            response = self.get(self._api_path + "tso_offers", params)
            return response.json()
        except ValueError as e:
            return {"error": e.args[0]}
    
    def imbalance_data(self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None):
        try:
            params: dict[str, str] = self._optional_date_range_params(start_date, end_date)
            response = self.get(self._api_path + "imbalance_data", params, {"Accept": "application/json"})
            return response.json()
        except ValueError as e:
            return {"error": e.args[0]}
    
    def _optional_date_range_params(self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None) -> dict[str, str]:
        params: dict[str, str] = {}

        if start_date is not None and end_date is not None:
            params["start_date"] = start_date.strftime(self._date_time_format)
            params["end_date"] = end_date.strftime(self._date_time_format)
        elif start_date is None and end_date is None:
            pass # No params are provided, which is a correct usage of this API
        else:
            raise ValueError("Both start_date and end_date must be provided or not provided.")