def candle_strength(o,h,l,c):
    return abs(c-o)/(h-l+0.0001)

def rejection(o,h,l,c):

    if h-max(o,c) > 2*abs(c-o):
        return "BEARISH_REJECTION"

    if min(o,c)-l > 2*abs(c-o):
        return "BULLISH_REJECTION"

    return "NONE"

def breakout(prev_h,prev_l,h,l,c):

    if c > prev_h:
        return "UP"

    if c < prev_l:
        return "DOWN"

    return "NONE"