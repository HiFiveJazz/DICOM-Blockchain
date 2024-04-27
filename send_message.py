from web3 import Web3
infura_url = "..."
web3 = Web3(Web3.HTTPProvider(infura_url))
def debug():
    if web3.is_connected():
        print("Connected to node.")
        print("Block Number:", web3.eth.block_number)
        address = '0x32Be343B94f860124dC4fEe278FDCBD38C102D88'  # Example Infura address
        balance = web3.eth.get_balance(address)
        print("Balance:", web3.from_wei(balance, 'ether'), "ETH")
    else:
        print("Failed to connect to node.")# Displays the current block number we are on

debug()
