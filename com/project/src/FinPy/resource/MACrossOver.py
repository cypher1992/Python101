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
    context.snow= sid(43127)
    context.amd = sid(351)
    context.max_notional = 1000000

#Run trading program daily, one hour after market open.
    schedule_function(ma_crossover_handling,
                      date_rules.every_day(),
                      time_rules.market_open(hours=1))

#Daily price history XXXXXXX
def ma_crossover_handling(context, data):
    applHist = data.history(
        context.aapl,
        fields= 'price',
        bar_count=200,
        frequency='1d'
    )

    snowHist = data.history(
        context.snow,
        fields= 'price',
        bar_count=200,
        frequency='1d'
    )

    amdHist = data.history(
        context.amd,
        fields= 'price',
        bar_count=200,
        frequency='1d'
    )


 #Generating log of average of last 50 daily price data points.
    log.info(applHist.head())
    sma_200 = applHist.mean()
    sma_50 = applHist[-50:].mean()
    sma_7 = applHist[-7:].mean()

    log.info(snowHist.head())
    snsma_200 = snowHist.mean()
    snsma_50 = snowHist[-50:].mean()
    snsma_7 = snowHist[-7:].mean()

    log.info(amdHist.head())
    amdsma_200 = amdHist.mean()
    amdsma_50 = amdHist[-50:].mean()
    amdsma_7 = amdHist[-7:].mean()


#Returns all open orders.
    open_orders = get_open_orders()

#If no open orders, balance 100% of portfolio to AAPL &
#execute scheduled market order if SMA 15 is greater than SMA 50.
    if sma_50 > sma_200:
        if context.aapl not in open_orders:
            order_target_percent(context.aapl, 0.50)

    if snsma_50 > snsma_200:
        if context.snow not in open_orders:
            order_target_percent(context.snow, 0.25)

    if amdsma_50 > amdsma_200:
        if context.amd not in open_orders:
            order_target_percent(context.amd, 0.25)

#If no open orders, short sell 100% of portfolio of AAPL &
#execute scheduled market order if SMA 50 is greater than SMA 15.
    elif sma_200 > sma_7:
        if context.aapl not in open_orders:
            order_target_percent(context.aapl, -0.50)

    elif snsma_200 > snsma_7:
        if context.snow not in open_orders:
            order_target_percent(context.snow, -0.25)

    elif amdsma_200 > amdsma_7:
        if context.amd not in open_orders:
            order_target_percent(context.amd, -0.25)

#Generates leverage chart.
    record(leverage = context.account.leverage)