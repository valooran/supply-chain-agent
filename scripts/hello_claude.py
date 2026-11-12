import json

from supply_agent.llm import ask_claude

system = "You are a supply chain assistant. Reply with valid JSON only, no other text."
prompt = (
    'Extract the PO number and status from this note: '
    '"PO-1042 from Acme Steel is 5 days late." '
    'Return JSON like {"po_number": "...", "status": "..."}'
)

reply = ask_claude(system, [{"role": "user", "content": prompt}])

# Models sometimes wrap JSON in ```json fences, so strip them
cleaned = reply.strip().removeprefix("```json").removesuffix("```").strip()
data = json.loads(cleaned)

print("PO:", data["po_number"])
print("Status:", data["status"])