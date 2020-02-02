from numpy import linalg as LA
import numpy as np


# Put any initialization logic here.  The context object will be passed to
# the other methods in your algorithm.
def initialize(context):
    context.stocks = [sid(2518), sid(5692), sid(16841), sid(19831), sid(5061),
                      sid(3735), sid(25317), sid(6984), sid(1900), sid(13905)]
    # context.stocks = []
    context.max_notional = 1000000
    context.previous_prices = None
    context.day = None

    schedule_function(execute, date_rules.every_day())


def execute(context, data):
    if context.previous_prices == None:
        context.previous_prices = np.array([data.current(stock, 'price') for stock in context.stocks])
        return

    if context.day == None:
        context.day = data.current(context.stocks[0], 'last_traded').day
        return

    if data.current(context.stocks[0], 'last_traded').day == get_datetime().day:
        return

    # calculate and shift change from previous days price
    current_prices = np.array([data.current(stock, 'price') for stock in context.stocks])

    pct_change = current_prices / context.previous_prices - 1

    gains = pct_change * (pct_change > 0)
    loss = pct_change * (pct_change <= 0)
    # normalize

    norm_gains = gains / LA.norm(gains)
    norm_loss = loss / LA.norm(loss)

    free_cash = context.portfolio.cash * 0.9

    for i in range(len(norm_gains)):
        stock = context.stocks[i]
        sell_amount = round(-1 * context.portfolio.positions[stock].amount * (norm_gains[i] ** 2))

        if norm_gains[i] > 0 and abs(sell_amount) > 0:
            if norm_gains[i] ** 2 > 0.33:
                order(stock, sell_amount)

    for i in range(len(norm_loss)):
        stock = context.stocks[i]

        buy_amount = round((free_cash / data.current(stock, 'price')) * (norm_loss[i] ** 2))
        if norm_loss[i] < 0 and abs(buy_amount) > 0:
            if norm_loss[i] ** 2 > 0.33:
                order(stock, buy_amount)

    context.previous_prices = current_prices
    context.day = data.current(context.stocks[0], 'last_traded').day