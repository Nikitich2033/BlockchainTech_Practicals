import json
import requests
from web3 import Web3, HTTPProvider

ETHERSCAN_API_KEY = ""
INFURA_URL = ""


def get_pair_abi_etherscan(pair_address, api_key):
    # The Contract Application Binary Interface (ABI) is the standard way to interact with contracts in the Ethereum ecosystem,
    # both from outside the blockchain and for contract-to-contract interaction.
    # Fetch the contract ABI from Etherscan
    abi_url = f"https://api.etherscan.io/api?module=contract&action=getabi&address={pair_address}&apikey={api_key}"
    response = requests.get(abi_url)
    abi_json = response.json()
    if "status" not in abi_json or abi_json["status"] != "1":
        print("Error fetching ABI:", abi_json)
        return None
    abi = abi_json["result"]
    # Parse the ABI into a JSON object
    pair_abi = json.loads(abi)
    return pair_abi


def get_name(contract_address, contract_abi):
    # Establish a connection with the Ethereum node
    web3 = Web3(HTTPProvider(INFURA_URL))

    # Instantiate the contract
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)

    # Get the token addresses
    token0_address = contract.functions.token0().call()
    token1_address = contract.functions.token1().call()

    # Now, to get the names of the tokens, we would need to call the 'name' function from each token's contract
    # For that we would need each token's ABI which should have the 'name' function,
    # for this example let's assume it's the same as for your contract

    token0 = web3.eth.contract(address=token0_address, abi=contract_abi)
    token1 = web3.eth.contract(address=token1_address, abi=contract_abi)

    token0_name = token0.functions.name().call()
    token1_name = token1.functions.name().call()

    return str(token0_name), str(token1_name)


if __name__ == "__main__":
    contract_address = Web3.to_checksum_address(
        "0x8BB53B95e8b7398fc9B4c11284dd94038aC0092E"
    )
    contract_abi = get_pair_abi_etherscan(contract_address, ETHERSCAN_API_KEY)
    print(get_name(contract_address, contract_abi))
