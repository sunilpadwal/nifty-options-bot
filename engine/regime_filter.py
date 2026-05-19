def detect_regime(mkt):

    move = abs(mkt["ltp"] - mkt["open"])
    range_ = mkt["high"] - mkt["low"]

    if move > 30 and range_ > 50:
        return "TREND"

    if range_ < 40:
        return "RANGE"

    if range_ > 80:
        return "VOLATILE"

    return "NORMAL"