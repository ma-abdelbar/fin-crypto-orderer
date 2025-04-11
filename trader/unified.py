# trader/unified.py

from .binance import BinanceTrader
from .bitget import BitgetTrader


class UnifiedTrader:
    def __init__(self, exchange: str):
        exchange = exchange.lower()

        if exchange == "testnet":
            self.trader = BinanceTrader(testnet=True)
        elif exchange == "binance":
            self.trader = BinanceTrader(testnet=False)
        elif exchange == "bitget":
            self.trader = BitgetTrader()
        else:
            raise ValueError(f"Unsupported exchange: {exchange}")

    def connect(self):
        self.trader.connect()

    def get_balance(self):
        return self.trader.get_balance()

    # def get_leverage(self, symbol="BTCUSDT"):
    #     return self.trader.get_leverage(symbol)
    
    def set_leverage(self, symbol="BTCUSDT", leverage=20):
        return self.trader.set_leverage(symbol, leverage)

    # def set_margin_mode(self, symbol="BTCUSDT", mode="cross"):
    #     if hasattr(self.trader, "set_margin_mode"):
    #         return self.trader.set_margin_mode(symbol=symbol, mode=mode)
    #     else:
    #         print("🔹 set_margin_mode skipped — not required on this exchange.")

    def set_position_mode(self, symbol="BTCUSDT", mode="double"):
        if hasattr(self.trader, "set_position_mode"):
            return self.trader.set_position_mode(symbol=symbol, mode=mode)
        else:
            print("🔹 set_position_mode skipped — not required on this exchange.")

    def place_entry_order(self, direction: str, price: float, quantity: float, symbol: str = "BTCUSDT"):
        return self.trader.place_entry_order(direction=direction, price=price, quantity=quantity, symbol=symbol)

    def place_sl_order(self, price: float, quantity: float, direction: str, symbol: str = "BTCUSDT"):
        return self.trader.place_sl_order(price=price, quantity=quantity, direction=direction, symbol=symbol)

    def place_tp_order(self, price: float, quantity: float, direction: str, symbol: str = "BTCUSDT"):
        return self.trader.place_tp_order(price=price, quantity=quantity, direction=direction, symbol=symbol)

    def place_limit_tp_order(self, price: float, quantity: float, direction: str, symbol: str = "BTCUSDT"):
        if hasattr(self.trader, "place_limit_tp_order"):
            return self.trader.place_limit_tp_order(price=price, quantity=quantity, direction=direction, symbol=symbol)
        else:
            raise NotImplementedError("place_limit_tp_order is not supported on this exchange.")
