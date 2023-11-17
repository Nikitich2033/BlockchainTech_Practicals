"""
A minimum working example to
fetch data from UNISWAP using graphQL
"""
import requests


RESERVE_QUERY = """
query {
  pools(first: 10) {
    id
    token1Price
    totalValueLockedToken0
    totalValueLockedToken1
    totalValueLockedUSDUntracked
  }
}
"""

URL = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3"

if __name__ == "__main__":
    r = requests.post(URL, json={"query": RESERVE_QUERY}, timeout=10)
    data = r.json()["data"]
    print(r.json()["data"])
