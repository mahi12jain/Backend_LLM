from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse

from models import QueryRequest
from llm import LLMAssistant
from query import EventGeneratorService

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Session-based conversation history
conversation_history = {}
    
# LLM Assistant and Event Generator
llm_assistant = LLMAssistant()
event_generator_service = EventGeneratorService(llm_assistant)

@app.post("/query")
async def process_query(request: QueryRequest):
    """
    Process user query with SSE streaming and tool calling
    """
    # Retrieve or initialize conversation history for this session
    if request.session_id not in conversation_history:
        conversation_history[request.session_id] = []

    # Add user query to conversation history
    conversation_history[request.session_id].append({
        "role": "user",
        "content": request.query
    })

    async def event_generator():
        async for event in event_generator_service.generate_events(
            conversation_history[request.session_id]
        ):
            # Add assistant message to conversation history if it's the final response
            if event.get('event') == 'end' and 'ai_response' in locals():
                conversation_history[request.session_id].append({
                    "role": "assistant",
                    "content": request.query
                })
            
            yield event

    return EventSourceResponse(event_generator())

@app.get("/health")
async def health_check():
    """Simple health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)