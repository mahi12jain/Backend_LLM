from typing import Dict, Any

def get_tools() -> list:
    """
    Define and return the list of available tools
    
    Returns:
        list: A list of tool definitions for the LLM assistant
    """
    return [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get current weather for a specified city",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {
                            "type": "string",
                            "description": "The city to get weather for"
                        }
                    },
                    "required": ["city"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_dealership_address",
                "description": "Get address for a specific dealership",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dealership_id": {
                            "type": "string",
                            "description": "Unique identifier for the dealership"
                        }
                    },
                    "required": ["dealership_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "check_appointment_availability",
                "description": "Check available appointment slots for a dealership on a specific date",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dealership_id": {
                            "type": "string",
                            "description": "Unique identifier for the dealership"
                        },
                        "date": {
                            "type": "string",
                            "description": "Date to check availability (YYYY-MM-DD)"
                        }
                    },
                    "required": ["dealership_id", "date"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "schedule_appointment",
                "description": "Schedule a test drive appointment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Unique identifier for the user"
                        },
                        "dealership_id": {
                            "type": "string",
                            "description": "Unique identifier for the dealership"
                        },
                        "date": {
                            "type": "string",
                            "description": "Appointment date (YYYY-MM-DD)"
                        },
                        "time": {
                            "type": "string",
                            "description": "Appointment time (HH:MM)"
                        },
                        "car_model": {
                            "type": "string",
                            "description": "Car model for the test drive"
                        }
                    },
                    "required": ["user_id", "dealership_id", "date", "time", "car_model"]
                }
            }
        }
    ]