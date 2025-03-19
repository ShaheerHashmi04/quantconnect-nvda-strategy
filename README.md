# quantconnect-nvda-strategy
A simple daily trading algorithm for NVDA using a moving average crossover strategy built in Python for QuantConnect. This strategy buys NVDA when the 10-day SMA crosses above the 30-day SMA and sells when the opposite occurs. Designed for backtesting and educational purposes.

# 📈 NVDA Moving Average Crossover Strategy

This repository contains a simple but effective **daily stock trading strategy** for NVIDIA Corp. (NVDA) using the **moving average crossover technique**. The strategy is implemented in Python and is designed to run on the [QuantConnect](https://www.quantconnect.com/) algorithmic trading platform.

## 💡 Strategy Overview

The strategy follows a **classic trend-following** logic using two Simple Moving Averages:

- **Fast Moving Average (SMA 10)**: Short-term price trend
- **Slow Moving Average (SMA 30)**: Long-term price trend

### ✅ Buy Signal:
When the 10-day SMA crosses **above** the 30-day SMA, it signals an **uptrend**, and the algorithm enters a long position on NVDA.

### ❌ Sell Signal:
When the 10-day SMA crosses **below** the 30-day SMA, it signals a **downtrend**, and the algorithm **exits** the position.

## ⚙️ How It Works

1. Loads historical daily data for NVDA.
2. Calculates 10-day and 30-day simple moving averages.
3. Checks for crossovers each day.
4. Enters or exits positions based on crossover signals.
5. Uses full portfolio allocation (100%) for trades.
6. Only trades long (no shorting).

## 🧪 Backtesting

This algorithm is intended for use on **QuantConnect’s backtesting engine**. You can run it by:

1. Creating a new project on QuantConnect (Python).
2. Copying the code from `nvda_moving_average_strategy.py`.
3. Running a backtest between any start and end dates.
4. Observing trade logs, performance metrics, and equity curve.

## 📁 File

- `nvda_moving_average_strategy.py`: The main trading algorithm script.

## 📊 Requirements

- QuantConnect account (free or paid)
- Internet access to run the backtest in the QuantConnect web IDE

## ⚠️ Disclaimer

This project is for **educational purposes only** and does not constitute financial advice or a recommendation to buy/sell securities. Backtesting results do not guarantee future performance.

---

## 📬 Contact

For questions or collaboration, feel free to open an issue or reach out.
