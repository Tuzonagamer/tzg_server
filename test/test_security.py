from app.application.controlers.security.TokenValidator import TokenValidator
import pytest


def test_validate_token():

    worker_name = "test_worker"
    key = "test_key"
    token = "098164e3a7d4471c26142b594f35f5b87dda136a"

    token_validator = TokenValidator(key)

    is_valid = token_validator.check_token(worker_name, token)

    assert is_valid, "token validator is not working with valid tokens"


tokens_to_validate = [
    {
        "worker_name": "test_worker",
        "key": "test_key",
        "token": "098164e3a7d4471c26142b594f35f5b87dda136a",
        "valid": True
    },
    {
        "worker_name": "test_worker",
        "key": "test_key_2",
        "token": "3199ce79959fe7711cf0d113744c022b5570f814",
        "valid": True
    },
    {
        "worker_name": "test_worker_2",
        "key": "test_key",
        "token": "0e07c44f006f661b7e344331925ae44044a3c4c4",
        "valid": True
    },
    {
        "worker_name": "test_worker",
        "key": "test_key",
        "token": "0e07c44f006f661b7e344331925ae44044a3c4c4",
        "valid": False
    },
]

@pytest.mark.parametrize('tokens_to_validate', tokens_to_validate)
def test_validator_multiple_tokens(tokens_to_validate):
    
    worker_name = tokens_to_validate["worker_name"]
    key =  tokens_to_validate["key"]
    token = tokens_to_validate["token"]
    expected_result = tokens_to_validate["valid"]

    token_validator = TokenValidator(key)

    is_valid = token_validator.check_token(worker_name, token)

    assert is_valid == expected_result
