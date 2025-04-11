# 💸 fin-crypto-orderer (Binance & Bitget)

A unified, interactive GUI built in Jupyter for visualizing and placing laddered crypto orders with automatic SL/TP calculation and full exchange integration. Tested for Binance testnet and Bitget mainnet.

---

## 🔧 Features

✅ Drag-and-drop entry ladder with dynamic % allocation  
✅ Automatic SL and TP ladders based on risk profile  
✅ Leverage, position sizing, and margin calculation  
✅ Manual fill tracking to manage real-time positions  
✅ Fully unified backend (Binance Testnet, Bitget Live)  
✅ Bitget SDK bundled locally  
✅ Limit or trigger-based take profit options

---

## 📁 Project Structure

```
crypto-orderer/
│
├── ui.ipynb                # Interactive Jupyter-based GUI
│
├── trader/
│   ├── base.py             # Abstract interface
│   ├── binance.py          # Binance implementation (testnet/live)
│   ├── bitget.py           # Bitget implementation (UMCBL live)
│   ├── unified.py          # Switches between exchanges
│   ├── config.py           # Loads local API credentials
│   └── bitget_sdk/         # Vendor SDK (licensed)
│       └── ...             # Included Bitget REST client
│
├── requirements.txt        # pip install -r
└── README.md
```

---

## 🚀 Quick Start

1. Clone the repo:
```bash
git clone git@github.com:<your-username>/crypto-orderer.git
cd crypto-orderer
```

2. Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your API keys:
Create a file called `trader/.env`:
```env
BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret
BITGET_API_KEY=your_key
BITGET_API_SECRET=your_secret
BITGET_PASSPHRASE=your_pass
```

5. Launch Jupyter and open the app:
```bash
jupyter lab
```
Open `ui.ipynb` and start planning your orders.

---

## 📦 Exchange Support

| Exchange | Testnet | Live | SL/TP Type |
|----------|---------|------|------------|
| Binance  | ✅       | ✅    | Limit + Trigger |
| Bitget   | ❌       | ✅    | Limit + Plan |

---

## 🙏 Credits

Bitget SDK © [bitget-exchange-open-api-sdk](https://github.com/bitget-exchange/bitget-api-sdk-python)  
Modified and embedded under `trader/bitget_sdk/` for simplified import and usage.

---

## 📈 Future Plans

- Multiple open notebook instances with account isolation  
- Realtime open orders + fill tracking  
- TradingView chart integration  
- Strategy presets (DCA, scalps, pyramiding, etc.)
