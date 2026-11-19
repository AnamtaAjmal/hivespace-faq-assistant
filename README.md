# HiveSpace FAQ Assistant

## Project Overview
HiveSpace FAQ Assistant is an AI-powered customer support automation system built using n8n, Google Sheets, and Google Gemini API. It automatically answers customer questions using stored FAQs and creates support tickets when it cannot confidently answer a question.

## Features
- Receives customer questions through a Webhook.
- Retrieves FAQ data from Google Sheets.
- Matches customer questions with existing FAQs.
- Uses Google Gemini AI to generate answers for questions that do not have an exact FAQ match.
- Checks answer confidence before responding.
- Automatically creates a support ticket when confidence is below 0.7.
- Saves tickets as JSON files inside the `tickets` folder.
- Logs API errors in Google Sheets.
- Sends responses back to customers through the Webhook.

## Technologies Used
- n8n – Workflow automation
- Python – Ticket creation tool
- Google Sheets – FAQ storage and error logging
- Google Gemini API – AI-powered responses
- JavaScript – Data processing and confidence checking
- JSON – Ticket storage and workflow export

## Project Structure

```text
hivespace-faq-assistant/
│
├── workflow.json
├── ticket_tool.py
├── README.md
│
└── tickets/
    └── ticket_YYYYMMDD_HHMMSS.json
```

## Requirements
- Python 3
- Node.js and npm
- n8n
- Google account
- Google Gemini API key

## Installation and Setup

### 1. Install n8n

Install Node.js, then run:

```bash
npx n8n
```

Open n8n in your browser:

```text
http://localhost:5678
```

### 2. Import the Workflow

1. Open n8n.
2. Import `workflow.json`.
3. Configure your Google Sheets credentials.
4. Configure your Gemini API credentials.
5. Verify the file path in the Execute Command node.

### 3. Run the Python Ticket Tool

Open CMD in the project folder and run:

```bash
python ticket_tool.py "I need help with membership"
```

The script automatically creates a `tickets` folder if it does not exist and saves a JSON ticket containing:

- Customer query
- Ticket status
- Creation timestamp

## Workflow Execution

1. Customer sends a question to the Webhook.
2. The workflow retrieves FAQ records from Google Sheets.
3. JavaScript checks for an exact FAQ match.
4. If an exact match exists, the stored answer is returned.
5. Otherwise, Gemini AI processes the question.
6. The Confidence Check evaluates the AI response.
7. If confidence is below 0.7, the Execute Command node runs `ticket_tool.py`.
8. A support ticket is saved as a JSON file.
9. The customer receives a response.

## Testing

**Test 1: Known FAQ**

Send a question that exists in Google Sheets.

Expected result: The assistant returns the matching FAQ answer.

**Test 2: Unknown FAQ**

Send a question that is not available in Google Sheets.

Expected result: Gemini processes the question. If confidence is below 0.7, a support ticket is automatically created.

## Security
- Keep API keys private.
- Do not upload API keys or passwords to GitHub.
- Configure credentials securely inside n8n.

## Author
Software Engineering Student

**Project:** HiveSpace FAQ Assistant  
**Purpose:** AI-powered FAQ automation and support ticket creation.
