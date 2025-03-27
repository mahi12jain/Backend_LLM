from groq import Groq
from groq.types.chat import ChatCompletion
import os
from dotenv import load_dotenv
from typing import List, Dict

from get_tools import get_tools 

class LLMAssistant:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Initialize Groq client
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        
        # Get tools from the separate module
        self.tools = get_tools()

    def generate_response(self, messages: List[Dict[str, str]]) -> ChatCompletion:
        """
        Generate a response using Groq API with tool calling support
        
        Args:
            messages (List[Dict[str, str]]): List of conversation messages
        
        Returns:
            ChatCompletion: The generated chat completion response
        """
        # Define system prompt to guide the model's responses
        system_prompt = {
            "role": "system", 
            "content": """You are a helpful virtual sales assistant for SuperCar dealerships. 
            When tools provide information:
            - For appointment availability, explain the available time slots
            - For dealership address, provide the full address details
            - For weather, give a concise weather report
            - Always be helpful and encourage booking a test drive
            
            Respond directly to the user's query using the tool information."""
        }
        
        # Prepend system prompt to messages
        enhanced_messages = [system_prompt] + messages

        # Generate response using Groq API
        return self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=enhanced_messages,
            tools=self.tools,
            tool_choice="auto"
        )