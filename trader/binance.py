# trader/binance.py

from binance.client import Client
from .config import get_binance_config
from .base import BaseTrader
from trader.utils import TICK_SIZE, LOT_SIZE_STEP, snap2step


class BinanceTrader(BaseTrader):
    def __init__(self, testnet=False):
        self.testnet = testnet
        self.config = get_binance_config(testnet)
        self.client = None

    def connect(self):
        self.client = Client(self.config.api_key, self.config.api_secret, testnet=self.testnet)
        if self.testnet:
            self.client.FUTURES_URL = self.config.base_url
        print("Connected to Binance", "(testnet)" if self.testnet else "")

    def get_balance(self):
        print("Using testnet base URL:", self.client.FUTURES_URL)
        account_info = self.client.futures_account_balance()
        usdt = next((b for b in account_info if b['asset'] == 'USDT'), None)
        return float(usdt['balance']) if usdt else 0.0

    def set_leverage(self, symbol='BTCUSDT', leverage=1):
        return self.client.futures_change_leverage(symbol=symbol, leverage=leverage)

    # def get_leverage(self, symbol='BTCUSDT'):
    #     positions = self.client.futures_position_information(symbol=symbol)
    #     return int(positions[0]['leverage']) if positions else 0

    # === Unified Format === #

    def place_entry_order(self, direction: str, price: float, quantity: float, symbol="BTCUSDT"):
        side = 'BUY' if direction == 'Long' else 'SELL'

        order = {
            'symbol': symbol,
            'side': side,
            'type': 'LIMIT',
            'price': snap2step(price, TICK_SIZE),
            'quantity': snap2step(quantity, 0.001),
            'timeInForce': 'GTC',
            'reduceOnly': False
        }

        print("📈 Entry order:", order)
        return self.client.futures_create_order(**order)



    def place_sl_order(self, price: float, quantity: float, direction: str, symbol="BTCUSDT", reduce_only=True):
        side = "SELL" if direction == "Long" else "BUY"

        order = {
            "symbol": symbol,
            "side": side,
            "type": "STOP_MARKET",
            "stopPrice": snap2step(price, TICK_SIZE),
            "quantity": snap2step(quantity, 0.001),
            "timeInForce": "GTC",
            "reduceOnly": reduce_only
        }

        print(f"📉 SL order ({side}):", order)
        return self.client.futures_create_order(**order)


    def place_tp_order(self, price: float, quantity: float, direction: str, symbol: str = "BTCUSDT"):
        side = "SELL" if direction.upper() == "LONG" else "BUY"
        
        order = {
            "symbol": symbol,
            "side": side,
            "type": "TAKE_PROFIT_MARKET",  # ✅ This is the correct TP type for Binance
            "stopPrice": snap2step(price, TICK_SIZE),  # ✅ Must include trigger (stop) price
            "quantity": snap2step(quantity, 0.001),
            "timeInForce": "GTC",
            "reduceOnly": True
        }

        print(f"🎯 TP plan order ({side}):", order)
        return self.client.futures_create_order(**order)

        
    def place_limit_tp_order(self, price: float, quantity: float, direction: str, symbol: str = "BTCUSDT"):
        side = "SELL" if direction.upper() == "LONG" else "BUY"

        order = {
            "symbol": symbol,
            "side": side,
            "type": "LIMIT",
            "price": snap2step(price, TICK_SIZE),
            "quantity": snap2step(quantity, 0.001),
            "timeInForce": "GTC",
            "reduceOnly": True
        }

        print(f"🎯 LIMIT TP order ({side}):", order)
        return self.client.futures_create_order(**order)
