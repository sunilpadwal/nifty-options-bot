from telegram.ext import Application, CommandHandler
from data.breeze_client import BreezeClient
from engine.regime_filter import detect_regime
from engine.direction_filter import get_bias
from engine.strike_selector import select_strikes
from engine.entry_confirmation import EntryConfirmation

client = BreezeClient()
entry = EntryConfirmation()

async def search(update, context):

    spot = client.spot()
    chain = client.option_chain()

    mkt = {"ltp":spot,"open":spot,"high":spot,"low":spot}

    regime = detect_regime(mkt)

    if regime == "RANGE":
        await update.message.reply_text("🚫 No Trade Zone")
        return

    bias = get_bias(spot, chain)
    strikes = select_strikes(chain, spot)

    best = strikes[0]

    entry.set_signal(best["option"], bias, best["score"])

    await update.message.reply_text(f"""
🚀 SIGNAL READY

Bias: {bias}
Strike: {best["option"]["strike_price"]}
Score: {best["score"]}
""")

def start():
    app = Application.builder().token("YOUR_TOKEN").build()
    app.add_handler(CommandHandler("search", search))
    app.run_polling()