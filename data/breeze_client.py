from breeze_connect import BreezeConnect
from config import *

class BreezeClient:

    def __init__(self):
        self.connect()

    def connect(self):
        self.breeze = BreezeConnect(api_key=ICICI_API_KEY)
        self.breeze.generate_session(
            api_secret=ICICI_API_SECRET,
            session_token=ICICI_SESSION_TOKEN
        )

    def spot(self):
        data = self.breeze.get_quotes(
            stock_code="NIFTY",
            exchange_code="NSE"
        )
        return float(data["Success"][0]["ltp"])

    def option_chain(self):
        data = self.breeze.get_option_chain_quotes(
            stock_code="NIFTY",
            exchange_code="NFO",
            product_type="options"
        )
        return data["Success"]