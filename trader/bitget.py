# trader/bitget.py

from trader.bitget_sdk.v1.mix.order_api import OrderApi
from trader.bitget_sdk.v1.mix.account_api import AccountApi
from .config import get_bitget_config
from .base import BaseTrader
from trader.utils import TICK_SIZE, LOT_SIZE_STEP, snap2step


VERBOSE = False

class BitgetTrader(BaseTrader):
    def __init__(self):
        self.config = get_bitget_config()
        self.account_api = AccountApi(
            self.config.api_key,
            self.config.api_secret,
            self.config.passphrase
        )
        self.order_api = OrderApi(
            self.config.api_key,
            self.config.api_secret,
            self.config.passphrase
        )

    def connect(self):
        print("Bitget connected ✅")

    def get_balance(self):
        res = self.account_api.account({
            "symbol": "BTCUSDT_UMCBL",
            "marginCoin": "USDT"
        })
        if VERBOSE:
            print("Balance response (v1):", res)
        return float(res['data']['available']) if 'data' in res and 'available' in res['data'] else 0.0

    def set_leverage(self, symbol="BTCUSDT", leverage=20):
        symbol = f"{symbol}_UMCBL"
        res = self.account_api.setLeverage({
            "symbol": symbol,
            "marginCoin": "USDT",
            "leverage": str(leverage)
        })
        if VERBOSE:
            print("Set leverage response:", res)
        return res

    # def set_margin_mode(self, symbol="BTCUSDT", mode="crossed"):
    #     symbol = f"{symbol}_UMCBL"
    #     res = self.account_api.setMarginMode({
    #         "symbol": symbol,
    #         "marginCoin": "USDT",
    #         "marginMode": mode
    #     })
    #     print(f"✅ Margin mode set to '{mode}' for {symbol}")
    #     return res

    def set_position_mode(self, symbol="BTCUSDT", mode="double"):
        if mode not in ["single", "double"]:
            raise ValueError("Position mode must be 'single' or 'double'")
        hold_mode = "single_hold" if mode == "single" else "double_hold"
        symbol = f"{symbol}_UMCBL"
        payload = {
            "productType": "umcbl",
            "holdMode": hold_mode
        }
        print(f"⚙️ Setting position mode with:", payload)
        res = self.account_api.setPositionMode(payload)
        print(f"✅ Position mode set to '{mode}' with holdMode '{hold_mode}'")
        return res

    def place_entry_order(self, direction: str, price: float, quantity: float, symbol="BTCUSDT"):
        """
        direction: "Long" or "Short"
        """
        if direction not in ["Long", "Short"]:
            raise ValueError("direction must be 'Long' or 'Short'")

        bitget_side = "open_long" if direction == "Long" else "open_short"

        order = {
            "symbol": f"{symbol}_UMCBL",
            "marginCoin": "USDT",
            "size": str(quantity),
            "price": str(price),
            "side": bitget_side,
            "orderType": "limit"
        }

        if VERBOSE:
            print("📌 Submitting ENTRY order:")
            print(order)

        res = self.order_api.placeOrder(order)

        if VERBOSE:
            print("✅ ENTRY order response:", res)

        return res



    def place_sl_order(self, price: float, quantity: float, direction: str, symbol: str = "BTCUSDT"):
        """
        direction: "Long" or "Short"
        """
        if direction not in ["Long", "Short"]:
            raise ValueError("direction must be 'Long' or 'Short'")

        side = "close_long" if direction == "Long" else "close_short"

        order = {
            "symbol": f"{symbol}_UMCBL",
            "marginCoin": "USDT",
            "size": str(quantity),
            "triggerPrice": str(price),
            "planType": "normal_plan",
            "side": side,
            "orderType": "market",
            "triggerType": "fill_price",
        }

        if VERBOSE:
            print("📌 Submitting SL order:")
            print(order)

        res = self.order_api.placePlanOrder(order)

        if VERBOSE:
            print("✅ SL order response:", res)

        return res

    

    def place_tp_order(self, price: float, quantity: float, direction: str, symbol: str = "BTCUSDT"):
        """
        direction: "Long" or "Short"
        """
        if direction not in ["Long", "Short"]:
            raise ValueError("direction must be 'Long' or 'Short'")

        side = "close_long" if direction == "Long" else "close_short"

        order = {
            "symbol": f"{symbol}_UMCBL",
            "marginCoin": "USDT",
            "size": str(snap2step(quantity, LOT_SIZE_STEP)),
            "triggerPrice": str(snap2step(price, TICK_SIZE)),
            "planType": "normal_plan",
            "side": side,
            "orderType": "market",
            "triggerType": "fill_price",
            "reduceOnly": "true"
        }

        if VERBOSE:
            print("📌 Submitting TP order:")
            print(order)

        res = self.order_api.placePlanOrder(order)

        if VERBOSE:
            print("✅ TP order response:", res)

        return res

    def place_limit_tp_order(self, price: float, quantity: float, direction: str, symbol: str = "BTCUSDT"):
        """
        Places a reduce-only LIMIT TP order that shows on the chart and is movable.
        direction: 'Long' or 'Short'
        """
        if direction not in ["Long", "Short"]:
            raise ValueError("direction must be 'Long' or 'Short'")

        side = "close_long" if direction == "Long" else "close_short"

        order = {
            "symbol": f"{symbol}_UMCBL",
            "marginCoin": "USDT",
            "price": str(snap2step(price, TICK_SIZE)),
            "size": str(snap2step(quantity, LOT_SIZE_STEP)),
            "side": side,
            "orderType": "limit",
            "reduceOnly": "true"
        }

        if VERBOSE:
            print("📌 Submitting LIMIT TP order:")
            print(order)

        res = self.order_api.placeOrder(order)

        if VERBOSE:
            print("✅ LIMIT TP order response:", res)

        return res


