import json
from datetime import date

from supply_agent.llm import call_claude
from supply_agent.tools import TOOL_FUNCTIONS, TOOL_SCHEMAS

system = (
    f"You are a supply chain assistant. Today's date is {date.today().isoformat()}. "
    "Use the tools to answer. Don't guess."
)
messages = [{"role": "user", "content": "Are we low on stock for the items in late POs"}]

response = call_claude(system, messages, tools=TOOL_SCHEMAS)
print("Stop reason:", response.stop_reason)

if response.stop_reason == "tool_use":
    messages.append({"role": "assistant", "content": response.content})
    tool_results = []
    for block in response.content:
        if block.type == "tool_use":
            print(f"Claude asked for: {block.name}({block.input})")
            result = TOOL_FUNCTIONS[block.name](**block.input)
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": json.dumps(result),
            })
    messages.append({"role": "user", "content": tool_results})
    response = call_claude(system, messages, tools=TOOL_SCHEMAS)

for block in response.content:
    if block.type == "text":
        print(block.text)