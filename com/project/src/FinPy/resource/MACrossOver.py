"""
Algorithm investment thesis:
Momentum investing from simple moving average (SMA) signals will outperform market-at-large and/or simply holding long.

Every day, we long Apple if SMA 15 is greater than SMA 50, which signals upward price momentum.

We short Apple if SMA 50 is greater than SMA 15, which signals downward price momentum.

"""

#The initialize function sets any data or variables used in the algorithm.
#For the purpose of this article, we are comparing Apple to the North American technology sector benchmark.
def initialize(context):
    set_benchmark(symbol('SPY'))
    context.aapl= sid(24)
    context.max_notional = 1000000

#Run trading program daily, one hour after market open.
    schedule_function(ma_crossover_handling,
                      date_rules.every_day(),
                      time_rules.market_open(hours=1))

#Daily price history XXXXXXX
def ma_crossover_handling(context, data):
    hist = data.history(
        context.aapl,
        fields= 'price',
        bar_count=200,
        frequency='1d'
    )
 #Generating log of average of last 50 daily price data points.
    log.info(hist.head())
    sma_200 = hist.mean()
    sma_50 = hist[-50:].mean()
    sma_7 = hist[-7:].mean()

#Returns all open orders.
    open_orders = get_open_orders()

#If no open orders, balance 100% of portfolio to AAPL &
#execute scheduled market order if SMA 15 is greater than SMA 50.
    if sma_50 > sma_200:
        if context.aapl not in open_orders:
            order_target_percent(context.aapl, 1.0)

#If no open orders, short sell 100% of portfolio of AAPL &
#execute scheduled market order if SMA 50 is greater than SMA 15.
    elif sma_200 > sma_7:
        if context.aapl not in open_orders:
            order_target_percent(context.aapl, -1.0)

#Generates leverage chart.
    record(leverage = context.account.leverage)