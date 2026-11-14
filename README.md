# hives# HiveSpace Coworking FAQ Assistant

## Project Overview
HiveSpace Coworking FAQ Assistant is an automation project built using n8n. Its purpose is to receive customer questions through a webhook and prepare them for further processing.

## Technologies Used
- n8n
- Git and GitHub
- Node.js
- curl

## Task 1: Basic Webhook Workflow
This task implements a basic n8n workflow containing:

1. **Webhook Node:** Receives customer questions through POST requests.
2. **Edit Fields (Set) Node:** Extracts the incoming question and stores it in a field named `customer_question`.

## Webhook Configuration
- HTTP Method: POST
- Webhook Path: `hive-faq`
- Authentication: None

## Testing
Start n8n locally:

```bash
npx n8n
```

Open the n8n editor at `http://localhost:5678`.

Send a test request using curl:

```bash
curl -X POST http://localhost:5678/webhook-test/hive-faq -H "Content-Type: application/json" -d "{\"question\":\"What are your membership prices?\"}"
```

Expected output in the Edit Fields node:

```json
{
  "customer_question": "What are your membership prices?"
}
```

## Project Files
- `README.md` — Project documentation.
- `workflow.json` — Exported n8n workflow.

## Current Progress
Task 1: Basic n8n webhook workflow completed and tested locally.pace-faq-assistant
