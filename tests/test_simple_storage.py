from brownie import accounts, config, SimpleStorage


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def test_update():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    simple_storage.store(69, {"from": account})
    expected = 9
    # Assert
    assert simple_storage.retrieve() == expected
