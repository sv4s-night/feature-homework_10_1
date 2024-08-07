from src.widget import get_data, mask_account_card


def test_mask_account_card(fixture_test_mask_account_card, fixture_test_get_mask_account):
    assert mask_account_card(fixture_test_mask_account_card) == "1111 22** **** 4444"
    assert mask_account_card(fixture_test_get_mask_account) == "XXXX4321"


def test_get_data(fixture_test_get_data):
    assert get_data(fixture_test_get_data) == "12.09.2018"
