from os import getenv
from rte_api import WholesaleMarketAPI
from dotenv import load

load()

client_id = getenv("RTE_CLIENT_ID", "")
client_secret = getenv("RTE_CLIENT_SECRET", "")

api = WholesaleMarketAPI(client_id, client_secret)

print(api.france_power_exchanges())