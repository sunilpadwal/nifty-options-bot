def get_bias(spot, chain):

    call = sum(o.get("change_in_oi",0) for o in chain if o.get("option_type")=="CE")
    put = sum(o.get("change_in_oi",0) for o in chain if o.get("option_type")=="PE")

    if call > put:
        return "BULLISH"

    if put > call:
        return "BEARISH"

    return "RANGE"