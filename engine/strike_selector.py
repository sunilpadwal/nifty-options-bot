def select_strikes(chain, spot):

    candidates = []

    for opt in chain:

        dist = abs(opt["strike_price"] - spot)

        if dist > 200:
            continue

        score = 0

        if dist < 50:
            score += 40

        score += min(opt.get("volume",0)/100,20)
        score += min(opt.get("open_interest",0)/5000,20)
        score += min(opt.get("change_in_oi",0)/500,20)

        candidates.append({
            "option": opt,
            "score": score
        })

    return sorted(candidates, key=lambda x: x["score"], reverse=True)[:3]