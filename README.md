# Backend_LLM

SuperCar Virtual Sales Assistant - Backend
Project Overview
This is a FastAPI backend for the SuperCar Virtual Sales Assistant, designed to provide an AI-powered chat interface for car dealership interactions. The backend supports streaming AI responses, tool calling with Groq API, and maintaining conversation context.
Features

Server-Sent Events (SSE) streaming of AI responses
Tool calling functionality using Groq API with Llama 3.3 70B Versatile
Conversation history management
CORS support
Docker Compose development environment

Implemented Tools

Weather Lookup

Get current weather for a specified city


Dealership Address Finder

Retrieve dealership location details


Appointment Management

Check appointment availability
Schedule test drive appointments



Prerequisites

Python 3.9+
Docker (recommended)
Groq API account and API key

Getting Started
Using Docker Compose (Recommended)

Clone the repository

bashCopygit clone https://github.com/your-username/supercar-backend.git
cd supercar-backend

Create a Groq API account


Visit https://console.groq.com/
Get your API key


Configure environment

bashCopycd backend
cp .env.sample .env
# Edit .env and add your Groq API key

Start the development environment

bashCopycd ../infrastructure
docker-compose up
Manual Setup

Install dependencies

bashCopypip install fastapi uvicorn sse-starlette pydantic python-dotenv groq

Create .env file

CopyGROQ_API_KEY=your_groq_api_key_here

Run the application

bashCopyuvicorn backend.main:app --reload
Project Structure
Copybackend/
├── main.py          # FastAPI application and endpoints
├── models.py        # Pydantic models
├── llm.py           # Groq API integration
├── tools/           # Tool implementations
│   ├── weather.py
│   ├── dealership.py
│   └── appointment.py
└── utils/           # Utility functions
API Endpoints
/query (POST)
Accepts user queries and streams AI responses via Server-Sent Events (SSE)
Request Body:

query: User's message (string)
session_id: Conversation session identifier (string)

Response:

Streaming events for:

Text chunks
Tool usage
Tool outputs
Response completion



Development Notes

The system uses Llama 3.3 70B Versatile for AI interactions
Tool calling is implemented using Groq API
Conversation context is maintained per session

Testing

With Docker:

bashCopydocker-compose logs -f backend

Manual cURL test:

bashCopycurl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is the weather in New York?", "session_id": "test-session"}'
Technology Stack

FastAPI
Groq API
SSE-Starlette
Pydantic
Python

