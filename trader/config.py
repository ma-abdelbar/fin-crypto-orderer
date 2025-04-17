import os
from dotenv import load_dotenv
from collections import namedtuple

load_dotenv()

# BinanceConfig structure
BinanceConfig = namedtuple("BinanceConfig", ["api_key", "api_secret", "base_url"])

def get_binance_config(testnet=False):
    if testnet:
        return BinanceConfig(
            api_key=os.getenv("BINANCE_API_KEY_TESTNET"),
            api_secret=os.getenv("BINANCE_API_SECRET_TESTNET"),
            base_url="https://testnet.binancefuture.com"
        )
    else:
        return BinanceConfig(
            api_key=os.getenv("BINANCE_API_KEY"),
            api_secret=os.getenv("BINANCE_API_SECRET"),
            base_url=""  # Use default mainnet endpoint
        )

# BitgetConfig structure
BitgetConfig = namedtuple("BitgetConfig", ["api_key", "api_secret", "passphrase"])

def get_bitget_config():
    return BitgetConfig(
        api_key=os.getenv("BITGET_API_KEY"),
        api_secret=os.getenv("BITGET_API_SECRET"),
        passphrase=os.getenv("BITGET_PASSPHRASE")
    )
