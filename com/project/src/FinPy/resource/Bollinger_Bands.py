import pandas


def initialize(context):
    context.stock = sid(28016)
    context.qty = 400
    context.stddev_limit = 1.75
    schedule_function(order_handling, date_rules.every_day())


def order_handling(context, data):
    current_price = data.current(context.stock, 'price')
    price_history = data.history(context.stock, 'price', 20, '1d')

    mean = price_history.mean()
    stddev = price_history.std()
    upper_bb = mean + 2 * stddev
    lower_bb = mean - 2 * stddev

    record(CMG=current_price)
    record(Upper=upper_bb)
    record(MA20=mean)
    record(Lower=lower_bb)

    # At top of bands?
    if current_price > mean + stddev * context.stddev_limit:
        # Are we long or neutral?
        if context.portfolio.positions[context.stock].amount >= 0:
            # Close our long position if we have one
            close_position(context, data)
            order(context.stock, -context.qty)
    # At bottom of bands?
    if current_price < mean - stddev * context.stddev_limit:
        # Are we short or neutral?
        if context.portfolio.positions[context.stock].amount <= 0:
            # Close our short position if we have one
            close_position(context, data)
            order(context.stock, context.qty)
        return


def close_position(context, data):
    # Open position?
    if context.portfolio.positions[context.stock].amount > 0:
        order(context.stock, -context.qty)
    elif context.portfolio.positions[context.stock].amount < 0:
        order(context.stock, context.qty)
    return