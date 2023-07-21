from brownie import accounts, config, SimpleStorage, network
import os


def deploy_simple_storage():
    # Deploying contract
    account = get_account
    simple_storage = SimpleStorage.deploy({"from": account})
    # Accessing the retrieve function of the SimpleStorage Contract
    tx = simple_storage.store(69, {"from": account})
    tx.wait(1)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    # account = accounts.load("Taimur")
    # print(account)
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # print(account)
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
