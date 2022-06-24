from web3 import Web3
import json

def run():
    abi = json.load(open('dep_contract.json', 'r'))
    w3 = Web3(Web3.HTTPProvider("https://mainnet-dev.deeper.network/rpc"))
    contract_instance = w3.eth.contract(address='0x60eF94dbbe8E80024Eff0693976Be26d27aEA746', abi=abi)

    transaction = contract_instance.functions.nNodeUnSpecifiedAddressTask('xcaptain/web3-demo2:arm64', '', 10, 10).buildTransaction({
        'gas': 228709,
        'nonce': w3.eth.get_transaction_count('0x27FdDEF298618B512Fa6D281DB0e32E0F38D15D3')
    })
    signed_tx = w3.eth.account.sign_transaction(transaction, '1cb032b0e578674397079c72a820b1463cf34116c2654964bc9d0a4022e66907')
    txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    return txn_receipt

if __name__ == '__main__':
    print(run())