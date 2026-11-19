
import sys
import json
from datetime import datetime, timezone
from pathlib import Path

# Get customer question
query = " ".join(sys.argv[1:]).strip()

if not query:
    print("Error: No question provided")
    sys.exit(1)

# Create tickets folder
ticket_folder = Path(__file__).parent / "tickets"
ticket_folder.mkdir(exist_ok=True)

# Create ticket data
ticket = {
    "query": query,
    "status": "open",
    "created_at": datetime.now(timezone.utc).isoformat()
}

# Save ticket as JSON file
filename = datetime.now(timezone.utc).strftime("ticket_%Y%m%d_%H%M%S_%f.json")
ticket_file = ticket_folder / filename

with open(ticket_file, "w", encoding="utf-8") as file:
    json.dump(ticket, file, indent=4)

print(f"Ticket created successfully: {ticket_file}")
