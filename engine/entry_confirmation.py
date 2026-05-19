from engine.candle_filter import *

class EntryConfirmation:

    def __init__(self):
        self.pending = None

    def set_signal(self, opt, bias, score):

        self.pending = {
            "opt": opt,
            "bias": bias,
            "score": score
        }

    def confirm(self, mkt, prev):

        if not self.pending:
            return None

        o,h,l,c = mkt["open"],mkt["high"],mkt["low"],mkt["ltp"]

        if candle_strength(o,h,l,c) < 0.4:
            return "WEAK"

        if self.pending["bias"]=="BULLISH" and rejection(o,h,l,c)=="BEARISH_REJECTION":
            self.pending=None
            return "CANCELLED"

        if self.pending["bias"]=="BEARISH" and rejection(o,h,l,c)=="BULLISH_REJECTION":
            self.pending=None
            return "CANCELLED"

        b = breakout(prev["high"],prev["low"],h,l,c)

        if (self.pending["bias"]=="BULLISH" and b=="UP") or \
           (self.pending["bias"]=="BEARISH" and b=="DOWN"):

            out=self.pending
            self.pending=None
            return {"ENTRY":out}

        return "WAIT"