from os import getenv
from rte_api import BalancingEnergyAPI, ContentType
from datetime import datetime
from zoneinfo import ZoneInfo
from dotenv import load

load()

client_id = getenv("RTE_CLIENT_ID", "")
client_secret = getenv("RTE_CLIENT_SECRET", "")

start_date = datetime(year=2023, month=10, day=1, tzinfo=ZoneInfo("Europe/Paris"))
end_date = datetime(year=2023, month=11, day=5, tzinfo=ZoneInfo("Europe/Paris"))
api = BalancingEnergyAPI(client_id, client_secret)

data = api.imbalance_data(start_date, end_date, ContentType.CSV)
print(data)