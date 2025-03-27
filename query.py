import asyncio
import json
from typing import Dict, List, AsyncGenerator

from models import ToolUseResponse
from llm import LLMAssistant
from tools.weather import get_weather
from tools.dealership import get_dealership_address
from tools.appointment import check_appointment_availability, schedule_appointment

class EventGeneratorService:
    def __init__(self, llm_assistant: LLMAssistant):
        """
        Initialize EventGeneratorService
        
        Args:
            llm_assistant (LLMAssistant): LLM Assistant instance
        """
        self.llm_assistant = llm_assistant

    async def generate_events(
        self, 
        conversation_history: List[Dict[str, str]]
    ) -> AsyncGenerator[Dict[str, str], None]:
        """
        Generate events for SSE streaming
        
        Args:
            conversation_history (List[Dict[str, str]]): Conversation history
        
        Yields:
            Dict[str, str]: Events for streaming
        """
        try:
            # Get LLM response
            response = self.llm_assistant.generate_response(conversation_history)

            # Ensure we have a message and extract tool calls
            message = response.choices[0].message
            tool_calls = message.tool_calls or []

            # Process tool calls
            for tool_call in tool_calls:
                async for event in self._process_tool_call(tool_call):
                    yield event

            # Generate AI response
            ai_response = message.content or "I'm ready to help you!"

            # Stream AI response chunks
            async for chunk in self._stream_ai_response(ai_response):
                yield chunk

        except Exception as e:
            # Comprehensive error handling
            yield {
                "event": "error",
                "data": f"Unexpected error: {str(e)}"
            }

    async def _process_tool_call(self, tool_call) -> AsyncGenerator[Dict[str, str], None]:
        """
        Process individual tool call
        
        Args:
            tool_call: Tool call from LLM response
        
        Yields:
            Dict[str, str]: Tool use and output events
        """
        tool_name = tool_call.function.name
        tool_args = json.loads(tool_call.function.arguments)

        # Yield tool use event
        yield {
            "event": "tool_use",
            "data": tool_name
        }

        # Execute tool based on name
        try:
            tool_output = await self._execute_tool(tool_name, tool_args)
            yield {
                "event": "tool_output",
                "data": ToolUseResponse(
                    name=tool_name, 
                    output=tool_output
                ).model_dump_json()
            }
        except Exception as tool_error:
            yield {
                "event": "tool_error",
                "data": f"Error in {tool_name}: {str(tool_error)}"
            }

    async def _execute_tool(self, tool_name: str, tool_args: Dict[str, str]):
        """
        Execute tool based on its name
        
        Args:
            tool_name (str): Name of the tool to execute
            tool_args (Dict[str, str]): Arguments for the tool
        
        Returns:
            Tool execution result
        """
        if tool_name == "get_weather":
            return await get_weather(tool_args['city'])
        elif tool_name == "get_dealership_address":
            return get_dealership_address(tool_args['dealership_id'])
        elif tool_name == "check_appointment_availability":
            return check_appointment_availability(
                tool_args['dealership_id'], 
                tool_args['date']
            )
        elif tool_name == "schedule_appointment":
            return schedule_appointment(
                tool_args['user_id'],
                tool_args['dealership_id'],
                tool_args['date'],
                tool_args['time'],
                tool_args['car_model']
            )
        else:
            return None

    async def _stream_ai_response(self, ai_response: str) -> AsyncGenerator[Dict[str, str], None]:
        """
        Stream AI response chunks
        
        Args:
            ai_response (str): AI-generated response
        
        Yields:
            Dict[str, str]: Response streaming events
        """
        if ai_response:
            for chunk in ai_response.split():
                yield {
                    "event": "chunk", 
                    "data": chunk + " "
                }
                await asyncio.sleep(0.1)  # Simulate streaming delay

        # End of response
        yield {
            "event": "end",
            "data": ""
        }