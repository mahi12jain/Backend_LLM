from typing import Dict, Any, List

def format_sse_event(event_type: str, data: Any) -> str:
    """
    Format an SSE event with type and data.
    """
    return f"event: {event_type}\ndata: {data}\n\n"

def serialize_tool_call(tool_call: Dict[str, Any]) -> str:
    """
    Serialize a tool call for SSE transmission.
    """
    return format_sse_event("tool_use", tool_call.get('function', {}).get('name', ''))

def serialize_tool_output(tool_name: str, output: Dict[str, Any]) -> str:
    """
    Serialize tool output for SSE transmission.
    """
    return format_sse_event("tool_output", {"name": tool_name, "output": output})