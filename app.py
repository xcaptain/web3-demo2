import requests
import json
import decimal
from web3 import Web3

def get_coin_price():
    r = requests.get('https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=DOT-USDT')
    return decimal.Decimal(r.json()['data']['price'])

def submit_price():
    abi = json.load(open('oracle_contract.json', 'r'))
    w3 = Web3(Web3.HTTPProvider("https://mainnet-dev.deeper.network/rpc"))
    contract_instance = w3.eth.contract(address='0x460E03e1e3551903456dC737a011D7B8da54e11c', abi=abi)

    new_price = int(1000000000000000000 * get_coin_price())
    transaction = contract_instance.functions.setTokenPrice(new_price).buildTransaction()
    transaction.update({ 'gas' : 140850 })
    transaction.update({ 'nonce' : w3.eth.get_transaction_count('0x27FdDEF298618B512Fa6D281DB0e32E0F38D15D3') })
    signed_tx = w3.eth.account.sign_transaction(transaction, '1cb032b0e578674397079c72a820b1463cf34116c2654964bc9d0a4022e66907')
    txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    return txn_receipt

if __name__ == '__main__':
    print(submit_price())