from dataclasses import dataclass, field
from os import getenv
from typing import Any, Dict, Optional

from agno.exceptions import ModelAuthenticationError
from agno.models.openai.like import OpenAILike


@dataclass
class Straitly(OpenAILike):
    """
    A class for interacting with models through Straitly, an OpenAI-compatible AI gateway.

    Straitly exposes an OpenAI-compatible Chat Completions API at
    https://api.straitly.ai/v1 for more than 150 models from providers including
    Anthropic, OpenAI, Google, xAI, and DeepSeek.

    Attributes:
        id (str): The id of the Straitly model to use. Defaults to "deepseek/deepseek-v4-1-flash-1017".
        name (str): The name of this chat model instance. Defaults to "Straitly".
        provider (str): The provider of the model. Defaults to "Straitly".
        api_key (Optional[str]): The API key to authorize requests to Straitly.
        base_url (str): The base URL to which requests are sent. Defaults to "https://api.straitly.ai/v1".
        max_tokens (Optional[int]): The maximum number of tokens. Defaults to None, so the
            parameter is omitted and the routed model's own output limit applies.
    """

    id: str = "deepseek/deepseek-v4-1-flash-1017"
    name: str = "Straitly"
    provider: str = "Straitly"
    api_key: Optional[str] = field(default_factory=lambda: getenv("STRAITLY_API_KEY"))
    base_url: str = "https://api.straitly.ai/v1"
    max_tokens: Optional[int] = None

    def _get_client_params(self) -> Dict[str, Any]:
        """
        Returns client parameters for API requests, checking for STRAITLY_API_KEY.

        Returns:
            Dict[str, Any]: A dictionary of client parameters for API requests.
        """
        if not self.api_key:
            self.api_key = getenv("STRAITLY_API_KEY")
            if not self.api_key:
                raise ModelAuthenticationError(
                    message="STRAITLY_API_KEY not set. Please set the STRAITLY_API_KEY environment variable.",
                    model_name=self.name,
                )
        return super()._get_client_params()
