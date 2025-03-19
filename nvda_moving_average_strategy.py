from AlgorithmImports import *

class NVDAMovingAverageCrossover(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2020, 1, 1)  # Set backtest start date
        self.SetEndDate(2023, 12, 31)  # Set backtest end date
        self.SetCash(100000)           # Starting capital

        self.symbol = self.AddEquity("NVDA", Resolution.Daily).Symbol

        # 10-day and 30-day simple moving averages
        self.fast_ma = self.SMA(self.symbol, 10, Resolution.Daily)
        self.slow_ma = self.SMA(self.symbol, 30, Resolution.Daily)

        # Use consolidator for daily bar updates
        self.last_action = None  # Track last action to avoid duplicates

    def OnData(self, data: Slice):
        # Wait until indicators are ready
        if not self.fast_ma.IsReady or not self.slow_ma.IsReady:
            return

        # Trading logic: crossover strategy
        holdings = self.Portfolio[self.symbol].Quantity

        if self.fast_ma.Current.Value > self.slow_ma.Current.Value and holdings <= 0:
            self.SetHoldings(self.symbol, 1.0)  # Long full position
            self.last_action = "Bought"
            self.Debug(f"BUY >> {self.Time.date()}, Price: {data[self.symbol].Price}")
        
        elif self.fast_ma.Current.Value < self.slow_ma.Current.Value and holdings > 0:
            self.Liquidate(self.symbol)
            self.last_action = "Sold"
            self.Debug(f"SELL >> {self.Time.date()}, Price: {data[self.symbol].Price}")
