//@version=5
indicator("Crypto Tradingview Signals", overlay=true)

// Get user input for symbol and timeframe
symbol = input(defval="BTC/USDT", title="Symbol")
timeframe = input(defval="1m", title="Timeframe")

// Moving average lengths
ma_length_50 = input(50, title="MA Length 50")
ma_length_200 = input(200, title="MA Length 200")
std_dev_length = input(20, title="Standard Deviation Length")

// Calculate moving averages
ma_50 = ta.sma(close, ma_length_50)  // Simple Moving Average (50)
ma_200 = ta.sma(close, ma_length_200) // Simple Moving Average (200)
std_dev = ta.stdev(close, std_dev_length) // Standard Deviation 

// Calculate buy and sell signals
buy_signal = ta.crossunder(ma_50, ma_200) and close < ma_50 - std_dev  // Buy when MA50 crosses below MA200 and price is low
sell_signal = ta.crossover(ma_50, ma_200) and close > ma_50 + std_dev  // Sell when MA50 crosses above MA200 and price is high

// Plot moving averages
plot(ma_50, color=color.blue, title="MA 50")
plot(ma_200, color=color.orange, title="MA 200")

// Plot buy and sell signals
plotshape(buy_signal, location=location.belowbar, color=color.green, style=shape.labelup, text="Buy")
plotshape(sell_signal, location=location.abovebar, color=color.red, style=shape.labeldown, text="Sell")

// Debugging output
if (buy_signal)
    label.new(bar_index, na, "Buy", color=color.green, style=label.style_label_down)

if (sell_signal)
    label.new(bar_index, na, "Sell", color=color.red, style=label.style_label_up)

// Alert on buy and sell signals
alertcondition(buy_signal, title="Buy Alert", message="Buy Signal Triggered: Consider Buying!")
alertcondition(sell_signal, title="Sell Alert", message="Sell Signal Triggered: Consider Selling!")