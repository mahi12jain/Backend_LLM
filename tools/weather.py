import httpx
from models import WeatherData

async def get_weather(city: str) -> WeatherData:
    """
    Mock weather retrieval function
    In a real implementation, this would call an external weather API
    """
    # Simulated weather data
    return WeatherData(
        temperature="34°C", 
        city=city,
        description="Sunny",
        humidity="45%"
    )