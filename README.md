# HiveSpace FAQ Assistant

## Project Overview

HiveSpace FAQ Assistant is an AI-powered customer support automation system developed using n8n, Google Sheets, Gemini AI, JavaScript, and Python.

The system automatically handles customer questions, searches frequently asked questions (FAQs), generates AI-based responses when needed, and creates support tickets when the AI cannot confidently answer a question.

The main goal of this project is to make customer support faster, easier, and more reliable through automation.

## Technologies Used

- **n8n:** Workflow automation platform.
- **Google Sheets:** Stores FAQ data and records API errors.
- **Google Gemini API:** Generates AI-based answers.
- **JavaScript:** Handles FAQ matching, response processing, and confidence checking.
- **Python:** Automatically creates support ticket files.
- **Webhook:** Receives customer questions through HTTP POST requests.

## Main Features

1. Receives customer questions through a webhook.
2. Searches the Google Sheets FAQ database.
3. Returns saved answers for exact FAQ matches.
4. Uses Gemini AI for questions that do not match existing FAQs.
5. Checks the confidence score of AI-generated responses.
6. Creates automatic support tickets for low-confidence answers.
7. Logs API errors in Google Sheets.
8. Returns responses to customers through the webhook.

## Workflow Explanation

The workflow follows these steps:

1. **Webhook:** Receives a customer's question.
2. **Edit Fields:** Extracts the customer question.
3. **Google Sheets:** Retrieves FAQ questions and answers.
4. **JavaScript:** Checks whether an exact FAQ match exists.
5. **If Node:** Routes the question according to the matching result.
6. **Gemini AI:** Generates an answer if no exact FAQ match is found.
7. **Parse Gemini Response:** Extracts the answer and confidence score.
8. **Confidence Check:** Checks whether the confidence score is below 0.7.
9. **If Node:** Routes the response to the appropriate branch.
10. **Execute Command:** Runs the Python script if confidence is below 0.7.
11. **Respond to Webhook:** Returns the appropriate response to the customer.

## Confidence Checking

The system uses a confidence threshold of **0.7**.

- If confidence is 0.7 or higher, the system returns the generated answer.
- If confidence is below 0.7, the system creates a support ticket using Python and informs the customer that a ticket has been created.

## Example Responses

### Example 1: Successful FAQ Response

**Customer Question:**

`Can I book a meeting room?`

**System Response:**

```json
{
  "answer": "Yes. Members can book meeting rooms subject to availability. Contact the front desk or use the booking process provided by HiveSpace.",
  "confidence": 0.95,
  "customer_question": "Can I book a meeting room?"
}
```

**Explanation:**

The question matches an existing FAQ in Google Sheets. The system returns the saved answer directly without calling Gemini AI.

### Example 2: Low-Confidence Response and Automatic Ticket Creation

**Customer Question:**

`Do you provide helicopter parking for members?`

**Customer Response:**

```json
{
  "answer": "I could not confidently answer your question. A support ticket has been created.",
  "ticket_details": "Ticket information returned by the Python script"
}
```

**What happens in the background?**

1. Gemini generates an answer with confidence below 0.7.
2. The If node checks the confidence score.
3. The Execute Command node runs the Python ticket creation script.
4. A timestamped support ticket is saved in the `tickets` folder.
5. The customer receives a message confirming ticket creation.

*Note: The ticket_details value above is illustrative. Actual output depends on the Python script.*

## Error Handling

The workflow includes an error-handling mechanism.

If the Gemini API request fails:

1. The error is routed to the Error Logger node.
2. The error message and timestamp are extracted.
3. The error information is stored in Google Sheets (Sheet2).

This helps keep a record of API errors for future investigation.

## Python Ticket Creation Tool

The project includes a Python script named `ticket_tool.py`.

Its responsibilities include:

- Receiving the customer's question.
- Handling empty input.
- Creating a timestamped support ticket.
- Saving the ticket as a file inside the `tickets` folder.

### Important Path Information

The Execute Command node uses local Windows paths to run Python and access `ticket_tool.py`.

These paths are specific to the development computer. If the workflow is imported on another computer, the Python executable path and script path must be updated accordingly.

## Project Requirements

- Windows operating system.
- Node.js and n8n.
- Python installed.
- Google account.
- Google Sheets.
- Google Gemini API key.
- Internet connection.

## Installation and Setup

### 1. Install n8n

Install and run n8n on your computer.

### 2. Import the Workflow

1. Open n8n.
2. Go to Workflows.
3. Select Import from File.
4. Select `workflow.json`.
5. Open the imported workflow.

### 3. Configure Credentials

Configure the following credentials in n8n:

- Google Sheets OAuth2 credential.
- Header Auth credential for Gemini API.

The Gemini API key is stored in the Header Auth credential instead of being written directly in the HTTP Request node.

If the workflow is imported into another n8n account, the credentials must be configured again.

### 4. Configure Python Paths

Check the Execute Command node and update the Python executable and `ticket_tool.py` paths according to your computer.

### 5. Activate the Workflow

Save the workflow and activate it in n8n.

## Testing the Workflow

The workflow can be tested using a POST request.

### Test Command

```cmd
curl -X POST http://localhost:5678/webhook-test/hive-faq -H "Content-Type: application/json" -d "{\"question\":\"Can I book a meeting room?\"}"
```

For the active workflow, use:

```cmd
curl -X POST http://localhost:5678/webhook/hive-faq -H "Content-Type: application/json" -d "{\"question\":\"Can I book a meeting room?\"}"
```

### Test Scenarios

1. **Existing FAQ:** Checks whether the system returns a saved answer.
2. **New Question:** Checks whether Gemini generates an answer.
3. **Low Confidence:** Checks whether a support ticket is created.
4. **API Error:** Checks whether the error is recorded in Google Sheets.

## Project Structure

```text
hivespace-faq-assistant/
│
├── workflow.json
├── ticket_tool.py
├── README.md
│
└── tickets/
    └── Generated support ticket files
```

## Security Notes

- Never share your Gemini API key publicly.
- Store API keys in n8n credentials.
- Do not upload API keys in workflow JSON files.
- Configure credentials securely after importing the workflow.
- Update local file paths when running the project on another computer.

## Project Objective

The objective of HiveSpace FAQ Assistant is to automate customer support by combining FAQ database searching, AI-generated answers, confidence checking, automatic ticket creation, and error logging in one workflow.

## Author

Software Engineering Student

**Project:** HiveSpace FAQ Assistant  
**Category:** AI and Workflow Automation
