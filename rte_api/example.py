from os import getenv
from balancing_energy import BalancingEnergyAPI
from datetime import datetime

client_id = getenv("RTE_CLIENT_ID", "")
client_secret = getenv("RTE_CLIENT_SECRET", "")

api = BalancingEnergyAPI(client_id, client_secret)

response = api.tso_offers(start_date=datetime(2025, 1, 1), end_date=datetime(2025, 6, 17))

print("Response with start and end dates:", response)

response = api.tso_offers()

print("Response with no dates:", response)