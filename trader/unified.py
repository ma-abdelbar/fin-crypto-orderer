# trader/unified.py

class UnifiedTrader:
    def __init__(self, exchange="testnet"):
        if exchange == "bitget":
            from .bitget import BitgetTrader
            self.trader = BitgetTrader()
        elif exchange == "binance":
            from .binance import BinanceTrader
            self.trader = BinanceTrader(testnet=False)
        elif exchange == "testnet":
            from .binance import BinanceTrader
            self.trader = BinanceTrader(testnet=True)
        else:
            raise ValueError("Unsupported exchange")
    
    def connect(self):
        self.trader.connect()

    def get_balance(self):
        return self.trader.get_balance()

    def set_leverage(self, symbol="BTCUSDT", leverage=20):
        return self.trader.set_leverage(symbol, leverage)

    def set_position_mode(self, symbol="BTCUSDT", mode="double"):
        return self.trader.set_position_mode(symbol, mode)

    def place_entry_order(self, direction, price, quantity, symbol="BTCUSDT", PosSL=None):
        return self.trader.place_entry_order(
            direction=direction,
            price=price,
            quantity=quantity,
            symbol=symbol,
            PosSL=PosSL
        )

    def place_sl_order(self, price, quantity, direction, symbol="BTCUSDT"):
        return self.trader.place_sl_order(price, quantity, direction, symbol)

    def place_tp_order(self, price, quantity, direction, symbol="BTCUSDT"):
        return self.trader.place_tp_order(price, quantity, direction, symbol)

    def place_limit_tp_order(self, price, quantity, direction, symbol="BTCUSDT"):
        return self.trader.place_limit_tp_order(price, quantity, direction, symbol)
