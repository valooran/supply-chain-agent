import anthropic

from supply_agent.config import get_settings


def ask_claude(system: str, messages: list[dict], max_tokens: int = 1024) -> str:
    settings = get_settings()
    client = anthropic.Anthropic(api_key=settings.api_key)
    response = client.messages.create(
        model=settings.model,
        max_tokens=max_tokens,
        system=system,
        messages=messages
    )
    return response.content[0].text

def call_claude(system: str, messages: list, tools: list | None = None, max_tokens: int = 1024):
    settings = get_settings()
    client = anthropic.Anthropic(api_key=settings.api_key)
    kwargs = dict(model=settings.model, max_tokens=max_tokens, system=system, messages=messages)
    if tools:
        kwargs["tools"] = tools
    return client.messages.create(**kwargs)