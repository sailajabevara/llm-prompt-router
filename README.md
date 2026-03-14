# LLM-Powered Prompt Router for Intent Classification

## Project Overview

This project implements an intelligent prompt routing system powered by a Large Language Model (LLM).  
Instead of using a single generic prompt, the system first **classifies the user's intent** and then routes the request to a specialized AI persona.

This approach improves response quality by using **expert prompts** tailored for specific tasks such as coding help, data analysis, writing improvement, and career advice.

The system follows a **two-step architecture**:
1. **Intent Classification**
2. **Prompt Routing and Response Generation**

---

## Architecture

The system workflow follows this pipeline:

User Message  
↓  
Intent Classifier (LLM)  
↓  
Detected Intent (code / data / writing / career / unclear)  
↓  
Router selects Expert Prompt  
↓  
LLM generates specialized response  
↓  
Response returned to user  
↓  
Request logged to `route_log.jsonl`

Components:

- **classifier.py** → Detects user intent
- **router.py** → Routes request to correct expert persona
- **prompts.py** → Stores system prompts for expert roles
- **logger.py** → Logs requests and responses
- **app.py** → Main application entry point

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd llm-prompt router
```
### 2. Install dependencies
pip install -r requirements.txt
### 3. Create environment file

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here

Do not commit this file to the repository.

### Running the Application

Run the application using:

python app.py

### You will see a prompt:

User:

Example interaction:

User: how do i sort a list in python?

Detected Intent: {'intent': 'code', 'confidence': 0.9}

Assistant:
You can sort a list in Python using sorted() or list.sort().

# To exit the application:

exit
### Docker Setup

You can also run the project using Docker.

Build and run the container
docker-compose up --build

# This will:

Build the Docker image

Install dependencies

Start the application

Supported Intents

### The system currently supports five intents:

Intent	Description
code	Programming and coding questions
data	Data analysis or statistical questions
writing	Writing improvement or grammar help
career	Career advice or job preparation
unclear	Messages that cannot be classified

Each intent routes to a specialized expert system prompt.

### Logging System

Every request is logged to a file called:

route_log.jsonl

## Each log entry contains:

intent
confidence
user_message
final_response

### Example log entry:

{"intent":"code","confidence":0.92,"user_message":"how do i sort a list in python","final_response":"Use sorted()..."}

The .jsonl format ensures that each line represents one request log.

### Testing

The application was tested using multiple inputs to verify correct intent routing.

# Example test messages:

how do i sort a list of objects in python?
I'm preparing for a job interview
Rewrite this sentence to be more professional
what is the average of 12 45 23 67
hey

### Expected intent outputs:

code
career
writing
data
unclear

All routing decisions were successfully logged in route_log.jsonl.

### Conclusion

This project demonstrates a practical LLM prompt routing architecture that improves response quality by using specialized expert prompts.

### Key features include:

Intent classification using LLM

Prompt routing to expert personas

Structured JSON output

Robust error handling

JSON Lines logging

Docker containerization

This architecture can be extended to support additional expert roles and integrated into larger AI-powered systems.