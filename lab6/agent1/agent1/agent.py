import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import LlmAgent


def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "den bosch":
        return {
            "status": "success",
            "report": "The weather in Den Bosch is sunny with 15°C."
        }
    elif city.lower() == "kandy":
        return {
            "status": "success",
            "report": "The weather in New York is sunny with 30°C."
        }
    return {
        "status": "error",
        "error_message": f"Weather for '{city}' unavailable."
    }


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg."""
    city_timezones = {
        "den bosch": "Europe/Amsterdam",
        "london": "Europe/London",
        "kandy": "Asia/Colombo",
        "paris": "Europe/Paris"
    }

    if city.lower() in city_timezones:
        try:
            tz = ZoneInfo(city_timezones[city.lower()])
            now = datetime.datetime.now(tz)
            return {
                "status": "success",
                "report": f"The current time in {city} is {now.strftime('%Y-%m-%d %H:%M:%S %Z')}"
            }
        except Exception as e:
            print(e)
            pass

    return {
        "status": "error",
        "error_message": f"Time information for '{city}' unavailable."
    }


# Define the agent with the name "root_agent" (required by ADK)
root_agent = LlmAgent(
    name="weather_time_agent",
    model="gemini-2.5-flash-lite",
    description="Agent that provides weather and time information for cities.",
    instruction="You help users with time and weather information for various cities.",
    tools=[get_weather, get_current_time],
)
