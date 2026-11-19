# HiveSpace FAQ Assistant

## Project Overview

HiveSpace FAQ Assistant is an AI-powered customer support automation system built using n8n. It helps customers get answers to frequently asked questions about HiveSpace services.

The system checks customer questions against stored FAQ data in Google Sheets. If an exact match is found, it returns the stored answer. If no exact match is found, it uses Google's Gemini AI to generate a response.

If the AI confidence score is below 0.7, the system automatically creates a support ticket using a Python script.

## Technologies Used

- **n8n:** Workflow automation
- **Google Sheets:** FAQ database and error logging
- **Google Gemini API:** AI-powered responses
- **Python:** Automatic support ticket creation
- **JavaScript:** FAQ matching and response processing
- **Webhook:** Receives customer questions

## Workflow Features

1. Receives customer questions through a POST webhook.
2. Retrieves FAQ records from Google Sheets.
3. Checks whether the question exactly matches an existing FAQ.
4. Returns the stored answer when an exact match is found.
5. Sends unmatched questions to Google Gemini.
6. Processes the AI response and checks its confidence score.
7. Creates a support ticket if confidence is below 0.7.
8. Logs HTTP Request errors in Google Sheets.
9. Returns the final response to the customer.

## Workflow Structure

```text
Webhook
   |
Edit Fields
   |
Get FAQ Data from Google Sheets
   |
FAQ Matching (JavaScript)
   |
Exact Match Check
   |
   |-- Exact Match --> Return FAQ Answer
   |
   |-- No Match --> Gemini API
                       |
                 Parse AI Response
                       |
                 Confidence Check
                       |
                    IF Node
                   /       \
            Below 0.7     0.7 or Above
                |              |
          Execute Command   Return Answer
                |
          Create Ticket
                |
          Return Response
```

## Project Setup

### 1. Requirements

- n8n installed on your computer
- Python installed
- Google account
- Google Sheets FAQ database
- Google Gemini API key

### 2. Import the Workflow

1. Open n8n.
2. Import the `workflow.json` file.
3. Open the Google Sheets nodes.
4. Connect your Google Sheets account.
5. Open the HTTP Request node.
6. Configure the Header Auth credential with your Gemini API key.

**API Key Security:** The Gemini API key is stored in n8n credentials and should never be added directly to the workflow JSON or uploaded to GitHub.

### 3. Python Ticket Tool Setup

The project includes a Python script named `ticket_tool.py`.

The Execute Command node runs this script when the AI confidence score is below 0.7.

**Important:** The Execute Command currently uses local Windows paths:

```cmd
"C:\Users\anamt\AppData\Local\Programs\Python\Python313\python.exe" "C:\Users\anamt\Documents\hivespace-faq-assistant\ticket_tool.py" "{{$json.customer_question}}"
```

These paths are specific to the developer's computer. If you run this project on another computer, update the Python executable path and project folder path according to your system.

### 4. Test the Workflow

Start the workflow in n8n and use the test webhook.

```cmd
curl -X POST http://localhost:5678/webhook-test/hive-faq -H "Content-Type: application/json" -d "{\"question\":\"Can I book a meeting room?\"}"
```

### 5. Example Response
### Example 2: Low-Confidence Response and Ticket Creation

**Customer Question:**

`Do you provide helicopter parking for members?`

**Customer Response:**

```json
{
  "answer": "I don't know",
  "confidence": 0.42,
  "customer_question": "Do you provide helicopter parking for members?"
}
```

**Automatic Ticket Creation:**

Because the confidence score (0.42) is below the threshold (0.7), the workflow:

1. Returns "I don't know" to the customer.
2. Executes the Python ticket creation script.
3. Creates a timestamped support ticket file in the `tickets` folder.

This fallback prevents the system from presenting an uncertain answer as reliable and records the unanswered question for further support.

*Note: The customer receives the response shown above. Ticket creation happens internally.*

```json
{
  "answer": "Yes. Members can book meeting rooms subject to availability. Contact the front desk or use the booking process provided by HiveSpace.",
  "confidence": 0.95,
  "customer_question": "Can I book a meeting room?"
}
```

## Support Ticket Automation

When Gemini returns a confidence score below 0.7, the workflow executes the Python ticket tool.

The script creates a ticket file in the project's `tickets` folder.

## Error Handling

If the Gemini HTTP Request fails, the workflow sends the error details to an Error Logger node and appends the information to Google Sheets.

## Project Files

```text
hivespace-faq-assistant/
|
|-- workflow.json
|-- ticket_tool.py
|-- README.md
|-- tickets/
```

## Security Notes

- Never upload API keys or passwords to GitHub.
- Use n8n credentials for API authentication.
- Keep credentials private.
- Update local file paths before running the workflow on another computer.

## Author

Software Engineering Student

## Project Purpose

This project demonstrates AI integration, workflow automation, FAQ management, API integration, error handling, and automated support ticket generation.
