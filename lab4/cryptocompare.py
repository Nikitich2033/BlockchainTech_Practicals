from pprint import pprint
import requests

datafolder = "data/"

BASEURL = "https://min-api.cryptocompare.com/data/v2/histohour?"


def getPriceHistory(fromcoin: str, limit: int = 2000, tocoin: str = "USD") -> None:
    url = f"{BASEURL}limit={limit}&tsym={tocoin}&fsym={fromcoin}"

    print(url)

    historyJSON = requests.get(url).json()

    pprint(historyJSON)

    return historyJSON


if __name__ == "__main__":
    data = getPriceHistory(fromcoin="ETH", limit=7)
    buffer = data["Data"]["Data"]
    # from volume and to volume
