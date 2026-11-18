# HiveSpace FAQ Assistant

## Project Overview
HiveSpace FAQ Assistant is an AI-powered customer support workflow built using n8n, Google Sheets, and the Gemini API. It answers customer questions using stored Frequently Asked Questions (FAQs).

## Features
- Loads FAQ questions and answers from Google Sheets.
- Receives customer questions through a Webhook.
- Uses the Gemini API to generate answers based on the FAQ data.
- Returns structured JSON containing an answer and confidence score.
- Checks the confidence score before providing an answer.
- Returns "I don't know" when confidence is below 0.7.
- Handles API errors through an error branch.

## Technologies Used
- n8n
- Google Sheets
- Google Gemini API
- JavaScript
- GitHub

## Workflow Overview
1. Webhook receives the customer's question.
2. Edit Fields prepares the customer question.
3. Google Sheets loads the FAQ data.
4. Code node combines FAQ rows and the customer question.
5. HTTP Request sends the question and FAQ data to Gemini.
6. A Code node parses the Gemini response.
7. Confidence Check validates the confidence score.
8. If confidence is below 0.7, the assistant returns "I don't know".
9. API errors are sent to the error-handling branch.

## Testing
The workflow was tested using mock responses:
- Confidence 0.5: Returns "I don't know".
- Confidence 0.8: Returns the generated answer.

## Error Handling
The HTTP Request node uses the error output to send API failures to the Error Logger branch.

## Project Files
- `workflow.json` – Initial Task 1 workflow.
- `HiveSpace FAQ Assistant.json` – Task 2 workflow.
- `sample_faq.xlsx` – Sample FAQ dataset.
- `README.md` – Project documentation.

## Note
The Gemini API key is kept private and is not included in the repository.# hives# HiveSpace Coworking FAQ Assistant

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
