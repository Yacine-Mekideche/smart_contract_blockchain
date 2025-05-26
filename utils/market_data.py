import requests

def get_token_data(token_id="tether"):
    """
    Récupère prix et market cap via l’API CoinGecko.
    """
    url = f"https://api.coingecko.com/api/v3/coins/{token_id}"
    try:
        d = requests.get(url).json()
        md = d["market_data"]
        return {
            "name": d["name"],
            "symbol": d["symbol"],
            "current_price": md["current_price"]["usd"],
            "market_cap": md["market_cap"]["usd"]
        }
    except:
        return {}
