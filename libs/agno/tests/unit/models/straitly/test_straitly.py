import os
from unittest.mock import patch

import pytest

from agno.exceptions import ModelAuthenticationError
from agno.models.straitly import Straitly
from agno.models.utils import get_model, get_model_from_dict


def test_straitly_initialization_with_api_key():
    model = Straitly(id="deepseek/deepseek-v4-1-flash-1017", api_key="test-api-key")
    assert model.id == "deepseek/deepseek-v4-1-flash-1017"
    assert model.api_key == "test-api-key"
    assert model.base_url == "https://api.straitly.ai/v1"


def test_straitly_initialization_without_api_key():
    with patch.dict(os.environ, {}, clear=True):
        model = Straitly(id="deepseek/deepseek-v4-1-flash-1017")
        client_params = None
        with pytest.raises(ModelAuthenticationError):
            client_params = model._get_client_params()
        assert client_params is None


def test_straitly_initialization_with_env_api_key():
    with patch.dict(os.environ, {"STRAITLY_API_KEY": "env-api-key"}):
        model = Straitly(id="deepseek/deepseek-v4-1-flash-1017")
        assert model.api_key == "env-api-key"


def test_straitly_client_params():
    model = Straitly(id="deepseek/deepseek-v4-1-flash-1017", api_key="test-api-key")
    client_params = model._get_client_params()
    assert client_params["api_key"] == "test-api-key"
    assert client_params["base_url"] == "https://api.straitly.ai/v1"


def test_straitly_default_values():
    model = Straitly(api_key="test-api-key")
    assert model.id == "deepseek/deepseek-v4-1-flash-1017"
    assert model.name == "Straitly"
    assert model.provider == "Straitly"
    assert model.max_tokens is None


def test_straitly_resolves_from_string_syntax():
    model = get_model("straitly:deepseek/deepseek-v4-1-flash-1017")
    assert isinstance(model, Straitly)
    assert model.id == "deepseek/deepseek-v4-1-flash-1017"


def test_straitly_round_trips_through_dict():
    model = Straitly(id="claude-sonnet-5-5", api_key="test-api-key")
    rebuilt = get_model_from_dict(model.to_dict())
    assert isinstance(rebuilt, Straitly)
    assert rebuilt.id == "claude-sonnet-5-5"
