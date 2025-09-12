from rte_api.common import RTEAPI
from datetime import datetime
from typing import Optional, Dict, Any

class WholesaleMarketAPI(RTEAPI):
    def __init__(self, client_id: str, client_secret: str):
        super().__init__(client_id, client_secret)
        self._api_path = "open_api/wholesale_market/v3/"

    def france_power_exchanges(self) -> Dict[str, Any]:
        """
        Returns day ahead french power exchange prices.
        """
        try:
            response = self.get(self._api_path + "france_power_exchanges")
            return response.json()
        except ValueError as e:
            return {"error": e.args[0]}